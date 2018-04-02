import unittest
import uuid

from db.card_dao import CardDao


class TestCardDao(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dao = CardDao("test_db")
        cls.dao.drop_db()

    def tearDown(self):
        self.dao.drop_decks()

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

    @unittest.skip("Not yet implemented")
    def test_delete_deck(self):
        deck_id = uuid.uuid4()
        name = "Mardu Moon"
        self.dao.create_deck(deck_id, name)
        self.dao.delete_deck(deck_id)

        deck = self.dao.get_deck(deck_id)
        self.assertIsNone(deck, "deck was still found after deletion")

    @unittest.skip("Not yet implemented")
    def test_delete_card_from_deck(self):
        deck_id = uuid.uuid4()
        name = "Mardu Moon"
        self.dao.create_deck(deck_id, name)
        card_id = "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e"
        self.dao.add_card(deck_id, card_id)

        deck = self.dao.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(1, len(cards))

        self.dao.delete_card_from_deck(deck_id, card_id)
        deck = self.dao.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(0, len(cards))
