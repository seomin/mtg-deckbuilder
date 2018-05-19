import unittest

from db.import_cards import import_cards
from db.operations.operations_factory import OperationsFactory
from errors.errors import DeckNotFoundError, CardNotFoundError

DB_NAME = "test_db"


class TestDeckOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        factory = OperationsFactory(DB_NAME)
        cls.deck_operations = factory.deck_operations
        card_operations = factory.card_operations
        factory.client.drop_database(DB_NAME)
        import_cards("XLN-x.json", card_operations)

    def setUp(self):
        self.deck_operations.drop_decks()

    def test_create_deck(self):
        name = "Riddledeck"
        deck_id = self.deck_operations.create_deck(name)
        deck = self.deck_operations.get_deck(deck_id)
        self.assertEqual(name, deck["name"], "wrong name")
        self.assertEqual(deck_id, deck["id"], "wrong id")

    def test_get_decks(self):
        name1 = "Riddledeck"
        self.deck_operations.create_deck(name1)
        name2 = "Mardu Moon"
        self.deck_operations.create_deck(name2)

        decks = self.deck_operations.get_decks()
        self.assertEqual(2, len(decks))

    def test_get_nonexisting_deck(self):
        deck_id = "some_id"
        with self.assertRaises(DeckNotFoundError):
            self.deck_operations.get_deck(deck_id)

    def test_add_card_to_deck(self):
        name = "Mardu Moon"
        deck_id = self.deck_operations.create_deck(name)

        # card_id is from Vona, Butcher of Magan
        card_id = "aa882bc018277cc70b06e643cd963360e590cc02"
        self.deck_operations.add_card_to_deck(deck_id, card_id)
        deck = self.deck_operations.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(1, len(cards))

    def test_add_card_to_nonexisting_deck(self):
        deck_id = "some_id"
        card_id = "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e"
        with self.assertRaises(DeckNotFoundError):
            self.deck_operations.add_card_to_deck(deck_id, card_id)

    def test_add_nonexisting_card_to_deck(self):
        name = "Riddledeck"
        deck_id = self.deck_operations.create_deck(name)
        card_id = "123"
        with self.assertRaises(CardNotFoundError):
            self.deck_operations.add_card_to_deck(deck_id, card_id)

    def test_delete_deck(self):
        name = "Mardu Moon"
        deck_id = self.deck_operations.create_deck(name)
        self.deck_operations.delete_deck(deck_id)

        with self.assertRaises(DeckNotFoundError, msg="deck was not deleted"):
            self.deck_operations.get_deck(deck_id)

    def test_delete_nonexisting_deck(self):
        deck_id = "some_id"
        with self.assertRaises(DeckNotFoundError):
            self.deck_operations.delete_deck(deck_id)

    def test_delete_card_from_deck(self):
        name = "Mardu Moon"
        deck_id = self.deck_operations.create_deck(name)

        # card_id is from Vona, Butcher of Magan
        card_id = "aa882bc018277cc70b06e643cd963360e590cc02"
        self.deck_operations.add_card_to_deck(deck_id, card_id)

        deck = self.deck_operations.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(1, len(cards))

        self.deck_operations.delete_card_from_deck(deck_id, card_id)
        deck = self.deck_operations.get_deck(deck_id)
        cards = deck["cards"]
        self.assertEqual(0, len(cards))

    def test_delete_nonexisting_card_from_deck(self):
        name = "Mardu Moon"
        deck_id = self.deck_operations.create_deck(name)
        card_id = "7788a85c7b2c420ad75719fe9a0e2e71a5eddc5e"

        with self.assertRaises(CardNotFoundError):
            self.deck_operations.delete_card_from_deck(deck_id, card_id)

    def test_card_tags(self):
        deck_name = "Mardu Moon"
        deck_id = self.deck_operations.create_deck(deck_name)
        # Vona, Butcher of Magan
        card_id = "aa882bc018277cc70b06e643cd963360e590cc02"
        self.deck_operations.add_card_to_deck(deck_id, card_id)

        card = self.deck_operations.get_card_from_deck(deck_id, card_id)
        self.assertEqual(0, len(card["tags"]), "New card should have 0 tags")

        # Add tags
        tags = ["manaSource", "ramp", "creature"]
        self.deck_operations.add_tags_to_card(deck_id, card_id, tags)

        card = self.deck_operations.get_card_from_deck(deck_id, card_id)
        tags = card["tags"]
        self.assertEqual(3, len(tags), "Wrong number of tags")
        self.assertTrue("manaSource" in tags)
        self.assertTrue("ramp" in tags)
        self.assertTrue("creature" in tags)

        # Delete tags
        tags_to_delete = ["ramp", "creature"]
        self.deck_operations.delete_tags_from_card(deck_id, card_id, tags_to_delete)

        card = self.deck_operations.get_card_from_deck(deck_id, card_id)
        tags = card["tags"]
        self.assertEqual(1, len(tags), "Wrong number of tags")
        self.assertTrue("manaSource" in tags)
