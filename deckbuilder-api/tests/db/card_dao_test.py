import unittest

from db.card_dao import CardDao
from db.import_cards import import_cards
from errors.errors import DeckNotFoundError, CardNotFoundError


class TestCardDao(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dao = CardDao("test_db")
        cls.dao.drop_db()
        import_cards("XLN-x.json", cls.dao)

    def setUp(self):
        self.dao.drop_decks()

    def test_create_deck(self):
        name = "Riddledeck"
        deck_id = self.dao.create_deck(name)
        deck = self.dao.get_deck(deck_id)
        self.assertEqual(name, deck["name"], "wrong name")
        self.assertEqual(deck_id, deck["id"], "wrong id")

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

        # card_id is from Vona, Butcher of Magan
        card_id = "aa882bc018277cc70b06e643cd963360e590cc02"
        self.dao.add_card_to_deck(deck_id, card_id)
        deck = self.dao.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(1, len(cards))

    def test_add_card_to_nonexisting_deck(self):
        deck_id = "some_id"
        card_id = "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e"
        with self.assertRaises(DeckNotFoundError):
            self.dao.add_card_to_deck(deck_id, card_id)

    def test_add_nonexisting_card_to_deck(self):
        name = "Riddledeck"
        deck_id = self.dao.create_deck(name)
        card_id = "123"
        with self.assertRaises(CardNotFoundError):
            self.dao.add_card_to_deck(deck_id, card_id)

    def test_delete_deck(self):
        name = "Mardu Moon"
        deck_id = self.dao.create_deck(name)
        self.dao.delete_deck(deck_id)

        with self.assertRaises(DeckNotFoundError, msg="deck was not deleted"):
            self.dao.get_deck(deck_id)

    def test_delete_nonexisting_deck(self):
        deck_id = "some_id"
        with self.assertRaises(DeckNotFoundError):
            self.dao.delete_deck(deck_id)

    def test_delete_card_from_deck(self):
        name = "Mardu Moon"
        deck_id = self.dao.create_deck(name)

        # card_id is from Vona, Butcher of Magan
        card_id = "aa882bc018277cc70b06e643cd963360e590cc02"
        self.dao.add_card_to_deck(deck_id, card_id)

        deck = self.dao.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(1, len(cards))

        self.dao.delete_card_from_deck(deck_id, card_id)
        deck = self.dao.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(0, len(cards))

    def test_delete_nonexisting_card_from_deck(self):
        name = "Mardu Moon"
        deck_id = self.dao.create_deck(name)
        card_id = "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e"

        with self.assertRaises(CardNotFoundError):
            self.dao.delete_card_from_deck(deck_id, card_id)

    def test_card_tags(self):
        deck_name = "Mardu Moon"
        deck_id = self.dao.create_deck(deck_name)
        # Vona, Butcher of Magan
        card_id = "aa882bc018277cc70b06e643cd963360e590cc02"
        self.dao.add_card_to_deck(deck_id, card_id)

        card = self.dao.get_card_from_deck(deck_id, card_id)
        self.assertEqual(0, len(card["tags"]), "New card should have 0 tags")

        # Add tags
        tags = ["manaSource", "ramp", "creature"]
        self.dao.add_tags_to_card(deck_id, card_id, tags)

        card = self.dao.get_card_from_deck(deck_id, card_id)
        tags = card["tags"]
        self.assertEqual(3, len(tags), "Wrong number of tags")
        self.assertTrue("manaSource" in tags)
        self.assertTrue("ramp" in tags)
        self.assertTrue("creature" in tags)

        # Delete tags
        tags_to_delete = ["ramp", "creature"]
        self.dao.delete_tags_from_card(deck_id, card_id, tags_to_delete)

        card = self.dao.get_card_from_deck(deck_id, card_id)
        tags = card["tags"]
        self.assertEqual(1, len(tags), "Wrong number of tags")
        self.assertTrue("manaSource" in tags)
