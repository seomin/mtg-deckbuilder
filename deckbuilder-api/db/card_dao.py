from pymongo import MongoClient
import re


class CardDao:
    _client = MongoClient()
    _db = _client.deckbuilder_db
    _all_cards = _db.all_cards

    def drop_cards(self):
        self._all_cards.drop()

    def save_card(self, card):
        self._all_cards.insert_one(card)

    def search_cards(self, search):
        cards = self._all_cards.find({"name": re.compile(search, re.IGNORECASE)}, {"_id": 0})
        return list(cards)
