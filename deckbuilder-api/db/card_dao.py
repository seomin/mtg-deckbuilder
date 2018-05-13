import re
import uuid

from pymongo import MongoClient

from db.entities.card_entity import CardEntity
from db.entities.deck_entity import DeckEntity
from errors.errors import DeckNotFoundError, CardNotFoundError
from util import mana_parser


class CardDao:
    def __init__(self, db_name):
        self.db_name = db_name
        self._client = MongoClient()
        self._db = self._client[db_name]
        self._all_cards = self._db.all_cards
        self._decks = self._db.decks

    def drop_db(self):
        self._client.drop_database(self.db_name)

    def drop_cards(self):
        self._all_cards.drop()

    def drop_decks(self):
        self._decks.drop()

    def save_card(self, card):
        self._all_cards.insert_one(card)

    def search_cards(self, search):
        if len(search) == 0:
            return list()
        cards = self._all_cards.find({"name": re.compile(search, re.IGNORECASE)}, {"_id": 0})
        return list(cards)

    def create_deck(self, name):
        deck_id = str(uuid.uuid4())
        # TODO Handle duplicate name
        new_deck = DeckEntity(deck_id, name)
        self._decks.insert_one(new_deck.__dict__)
        return deck_id

    def get_decks(self):
        decks = self._decks.find({}, {"_id": 0})
        return list(decks)

    def get_deck(self, deck_id):
        deck = self._decks.find_one({"id": deck_id}, {"_id": 0})
        if deck is None:
            raise DeckNotFoundError(deck_id)
        return deck

    def delete_deck(self, deck_id):
        deck = self._decks.find_one({"id": deck_id})
        if deck is None:
            raise DeckNotFoundError(deck_id)
        self._decks.delete_one({"id": deck_id})
        return deck

    def get_card_from_deck(self, deck_id, card_id):
        deck = self._decks.find_one({"id": deck_id})
        if deck is None:
            raise DeckNotFoundError(deck_id)
        for card in deck["cards"]:
            if card["id"] == card_id:
                return card
        raise CardNotFoundError(card_id)

    def add_card_to_deck(self, deck_id, card_id):
        deck = self._decks.find_one({"id": deck_id})
        if deck is None:
            raise DeckNotFoundError(deck_id)
        card = self._all_cards.find_one({"id": card_id})
        if card is None:
            raise CardNotFoundError(card_id)
        cards = list(deck["cards"])
        new_card = CardEntity(card_id, card["name"], card["mciUrl"], card["cmc"], card["manaCost"])
        cards.append(new_card.__dict__)

        # Update the CMC distribution
        cmc = deck["cmcDistribution"]
        cmc_card = card["cmc"]
        cmc_count = cmc.get(str(cmc_card), 0)
        cmc[str(cmc_card)] = cmc_count + 1

        # Update the Mana Color distribution
        mana_distribution_deck = deck["manaDistribution"]
        mana_distribution_card = card["manaCost"]
        cost = mana_parser.parse(mana_distribution_card)

        for key, value in mana_distribution_deck.items():
            mana_distribution_deck[key] = value + cost[key]

        self._decks.update_one({"id": deck_id}, {"$set": {"cards": cards, "cmcDistribution": cmc, "manaDistribution": mana_distribution_deck}})

    def delete_card_from_deck(self, deck_id, card_id):
        # First finding the deck
        deck = self._decks.find_one({"id": deck_id})
        cards = list(deck["cards"])

        # Finding the card
        card_index = None
        for index, card in enumerate(cards):
            if card["id"] == card_id:
                card_index = index
                break
        if card_index is None:
            raise CardNotFoundError(card_id)

        # Card exists, delete it from the list
        card = cards[card_index]
        del(cards[card_index])

        # Update the CMC distribution
        cmc = deck["cmcDistribution"]
        cmc_card = card["cmc"]
        cmc_count = cmc.get(str(cmc_card), 0)
        cmc[str(cmc_card)] = cmc_count - 1

        # Update the man cost distribution
        mana_distribution_deck = deck["manaDistribution"]
        mana_distribution_card = card["manaCost"]
        cost = mana_parser.parse(mana_distribution_card)

        for key, value in mana_distribution_deck.items():
            mana_distribution_deck[key] = value - cost[key]

        self._decks.update_one({"id": deck_id}, {"$set": {"cards": cards, "cmcDistribution": cmc, "manaDistribution": mana_distribution_deck}})
        return card

    def add_tags_to_card(self, deck_id, card_id, tags):
        deck = self._decks.find_one({"id": deck_id})
        cards = list(deck["cards"])

        found_card = False
        for card in cards:
            if card["id"] != card_id:
                continue

            found_card = True
            # We do not want to add duplicate tags, so first convert the tags to a set, which cannot contain duplicates
            card_tags = card["tags"]
            card_tags.extend(tags)
            card["tags"] = list(set(card_tags))
            break

        if not found_card:
            raise CardNotFoundError(card_id)

        self._decks.update_one({"id": deck_id}, {"$set": {"cards": cards}})

    def delete_tags_from_card(self, deck_id, card_id, tags_to_delete):
        deck = self._decks.find_one({"id": deck_id})
        cards = list(deck["cards"])

        found_card = False
        for card in cards:
            if card["id"] != card_id:
                continue

            found_card = True
            card_tags = card["tags"]
            for tag_to_delete in tags_to_delete:
                card_tags.remove(tag_to_delete)

            card["tags"] = card_tags
            break

        if not found_card:
            raise CardNotFoundError(card_id)

        self._decks.update_one({"id": deck_id}, {"$set": {"cards": cards}})
