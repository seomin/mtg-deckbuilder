import re


class CardOperations:
    def __init__(self, db):
        self._all_cards = db.all_cards

    def drop_cards(self):
        self._all_cards.drop()

    def save_card(self, card):
        self._all_cards.insert_one(card)

    def search_cards(self, search):
        if len(search) == 0:
            return list()
        cards = self._all_cards.find({"name": re.compile(search, re.IGNORECASE)}, {"_id": 0})
        return list(cards)