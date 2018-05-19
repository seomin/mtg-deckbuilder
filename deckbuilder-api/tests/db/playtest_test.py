import unittest

from db.import_cards import import_cards
from db.operations.operations_factory import OperationsFactory

DB_NAME = "test_db"


class PlaytestTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        factory = OperationsFactory(DB_NAME)
        cls.deck_operations = factory.deck_operations
        card_operations = factory.card_operations
        cls.playtest_operations = factory.playtest_operations
        factory.client.drop_database(DB_NAME)
        import_cards("XLN-x.json", card_operations)

    def setUp(self):
        self.deck_operations.drop_decks()

        name = "Chaos is Standard"
        self.deck_id = self.deck_operations.create_deck(name)

        # Vona, Butcher of Magan
        self.card_id1 = "aa882bc018277cc70b06e643cd963360e590cc02"
        # Bishop's Soldier
        self.card_id2 = "3587b6fecec7b71df3eb114c8638af927741a171"
        # Kitesail Freebooter
        self.card_id3 = "694cea4c33b1339bc798cc2b56f83e273c57cc11"

        self.deck_operations.add_card_to_deck(self.deck_id, self.card_id1)
        self.deck_operations.add_card_to_deck(self.deck_id, self.card_id2)
        self.deck_operations.add_card_to_deck(self.deck_id, self.card_id3)

    def test_move_cards_between_zones(self):
        pass


