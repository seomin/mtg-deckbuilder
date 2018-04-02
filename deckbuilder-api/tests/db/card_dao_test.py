import unittest

from db.card_dao import CardDao
from errors.errors import DeckNotFoundError, CardNotFoundError


class TestCardDao(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dao = CardDao("test_db")
        cls.dao.drop_db()

    def tearDown(self):
        self.dao.drop_decks()

    def test_create_deck(self):
        name = "Riddledeck"
        deck_id = self.dao.create_deck(name)
        deck = self.dao.get_deck(deck_id)
        self.assertEqual(name, deck["name"], "wrong name")
        self.assertEqual(deck_id, deck["id"], "wrong id")

    @unittest.skip("Not yet implemented")
    def test_get_decks(self):
        name1 = "Riddledeck"
        self.dao.create_deck(name1)
        name2 = "Mardu Moon"
        self.dao.create_deck(name2)

        decks = self.dao.get_decks()
        self.assertEqual(2, len(decks))

    def test_get_nonexisting_deck(self):
        deck_id = "some_id"
        with self.assertRaises(DeckNotFoundError):
            self.dao.get_deck(deck_id)

    def test_add_card_to_deck(self):
        name = "Mardu Moon"
        deck_id = self.dao.create_deck(name)
        card_id = "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e"
        self.dao.add_card(deck_id, card_id)
        deck = self.dao.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(1, len(cards))

    @unittest.skip("Not yet implemented")
    def test_add_card_to_nonexisting_deck(self):
        deck_id = "some_id"
        card_id = "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e"
        with self.assertRaises(DeckNotFoundError):
            self.dao.add_card(deck_id, card_id)

    def test_delete_deck(self):
        name = "Mardu Moon"
        deck_id = self.dao.create_deck(name)
        self.dao.delete_deck(deck_id)

        with self.assertRaises(DeckNotFoundError, msg="deck was not deleted"):
            self.dao.get_deck(deck_id)

    @unittest.skip("Not yet implemented")
    def test_delete_nonexisting_deck(self):
        deck_id = "some_id"
        with self.assertRaises(DeckNotFoundError):
            self.dao.delete_deck(deck_id)

    def test_delete_card_from_deck(self):
        name = "Mardu Moon"
        deck_id = self.dao.create_deck(name)
        card_id = "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e"
        self.dao.add_card(deck_id, card_id)

        deck = self.dao.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(1, len(cards))

        self.dao.delete_card_from_deck(deck_id, card_id)
        deck = self.dao.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(0, len(cards))

    @unittest.skip("Not yet implemented")
    def test_delete_nonexisting_card_from_deck(self):
        name = "Mardu Moon"
        deck_id = self.dao.create_deck(name)
        card_id = "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e"

        with self.assertRaises(CardNotFoundError):
            self.dao.delete_card_from_deck(deck_id, card_id)
