import unittest
import uuid

from db.card_dao import CardDao


class TestCardDao(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dao = CardDao("test_db")
        cls.dao.drop_db()

    def test_create_deck(self):
        _id = uuid.uuid4()
        name = "Riddledeck"
        self.dao.create_deck(_id, name)
        deck = self.dao.get_deck(_id)
        self.assertEqual(name, deck["name"], "wrong name")
        self.assertEqual(_id, deck["id"], "wrong id")

    def test_add_card_to_deck(self):
        deck_id = uuid.uuid4()
        name = "Mardu Moon"
        self.dao.create_deck(deck_id, name)
        self.dao.add_card(deck_id, "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e")
        deck = self.dao.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(1, len(cards))
