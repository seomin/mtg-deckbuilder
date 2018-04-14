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
        self.deck_id = self.dao.create_deck(name)

        # Vona, Butcher of Magan
        self.card_id1 = "aa882bc018277cc70b06e643cd963360e590cc02"

        # Bishop's Soldier
        self.card_id2 = "3587b6fecec7b71df3eb114c8638af927741a171"

        # Kitesail Freebooter
        self.card_id3 = "694cea4c33b1339bc798cc2b56f83e273c57cc11"
        self.dao.add_card_to_deck(self.deck_id, self.card_id1)
        self.dao.add_card_to_deck(self.deck_id, self.card_id2)
        self.dao.add_card_to_deck(self.deck_id, self.card_id3)

    def tearDown(self):
        self.dao.drop_decks()

    @classmethod
    def tearDownClass(cls):
        cls.dao.drop_db()

    def test_cmc_distribution(self):
        new_card_id = "0f232a33d864d2362389df5b3121139dd4b69ae5"

        deck = self.dao._decks.find_one({"id": self.deck_id})
        cmc = deck["cmc_distribution"]

        cmc_count = cmc.get("5", 0)
        self.assertEqual(1, cmc_count)

        self.dao.add_card_to_deck(self.deck_id, new_card_id)

        deck = self.dao._decks.find_one({"id": self.deck_id})
        cmc = deck["cmc_distribution"]

        cmc_count = cmc.get("5", 0)
        self.assertEqual(2, cmc_count)

        self.dao.delete_card_from_deck(self.deck_id, self.card_id1)

        deck = self.dao._decks.find_one({"id": self.deck_id})
        cmc = deck["cmc_distribution"]

        cmc_count = cmc.get("5", 0)
        self.assertEqual(1, cmc_count)