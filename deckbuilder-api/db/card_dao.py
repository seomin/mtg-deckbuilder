from pymongo import MongoClient
import re

from db.entities.deck_entity import DeckEntity


class CardDao:
    def __init__(self, db_name):
        self.db_name = db_name
        self._client = MongoClient()
        self._db = self._client[db_name]
        self._all_cards = self._db.all_cards
        self._decks = self._db.decks

    def save_card(self, card):
        self._all_cards.insert_one(card)

    def drop_db(self):
        self._client.drop_database(self.db_name)

    def drop_cards(self):
        self._all_cards.drop()

    def drop_decks(self):
        self._decks.drop()

    def create_deck(self, _id, name):
        new_deck = DeckEntity(_id, name)
        self._decks.insert_one(new_deck.__dict__)

    def search_cards(self, search):
        cards = self._all_cards.find({"name": re.compile(search, re.IGNORECASE)}, {"_id": 0})
        return list(cards)

    def get_deck(self, _id):
        deck = self._decks.find_one({"id": _id})
        return deck

    def delete_card_from_deck(self, deck_id, card_id):
        deck = self._decks.find_one({"id": deck_id})
        cards = list(deck["cards"])
        card_index = None
        for index, card in enumerate(cards):
            if card["id"] == card_id:
                card_index = index
                break
        if card_index is None:
            return None
        card = cards[card_index]
        del(cards[card_index])
        self._decks.update_one({"id": deck_id}, {"$set": {"cards": cards}})
        return card

    def add_card(self, deck_id, card_id):
        deck = self._decks.find_one({"id": deck_id})
        cards = list(deck["cards"])
        cards.append({"id": card_id})
        self._decks.update_one({"id": deck_id}, {"$set": {"cards": cards}})

    def delete_deck(self, deck_id):
        self._decks.delete_one({"id": deck_id})
