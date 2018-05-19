from pymongo import MongoClient

from db.operations.card_operations import CardOperations
from db.operations.deck_operations import DeckOperations
from db.operations.playtest_operations import PlaytestOperations


class OperationsFactory:
    def __init__(self, db_name):
        self.client = MongoClient()
        _db = self.client[db_name]
        self.deck_operations = DeckOperations(_db)
        self.card_operations = CardOperations(_db)
        self.playtest_operations = PlaytestOperations(_db)
