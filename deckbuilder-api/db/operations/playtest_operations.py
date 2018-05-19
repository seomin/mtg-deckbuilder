class PlaytestOperations:
    def __init__(self, db):
        self._decks = db.decks

    def move_cards_between_zones(self, deck_id, from_zone, to_zone, number_of_cards):
        pass

    def move_card_to_zone(self, deck_id, card_id, to_zone):
        pass

    def shuffle(self, deck_id, zone):
        pass

    def reveal(self, deck_id, zone, number_of_cards):
        pass
