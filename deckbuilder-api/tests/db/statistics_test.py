import unittest

from db.card_dao import CardDao
from db.import_cards import import_cards


class TestStatistics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dao = CardDao("test_db")
        import_cards("XLN-x.json", cls.dao)

    def setUp(self):
        name = "Chaos is Standard"
        deck_id = self.dao.create_deck(name)

        # Vrona, Butcher of Magan
        card_id1 = "aa882bc018277cc70b06e643cd963360e590cc02"

        # Bishop's Soldier
        card_id2 = "3587b6fecec7b71df3eb114c8638af927741a171"

        # Kitesail Freebooter
        card_id3 = "694cea4c33b1339bc798cc2b56f83e273c57cc11"
        self.dao.add_card(deck_id, card_id1)
        self.dao.add_card(deck_id, card_id2)
        self.dao.add_card(deck_id, card_id3)

    def tearDown(self):
        self.dao.drop_decks()

    @classmethod
    def tearDownClass(cls):
        cls.dao.drop_db()

    def test_cmc_distribution(self):
        pass
