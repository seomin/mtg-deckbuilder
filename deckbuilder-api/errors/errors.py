class Error(Exception):
    """Base class for errors"""
    pass


class NotFoundError(Error):
    """Some requested entity was not found"""
    pass


class DeckNotFoundError(NotFoundError):
    def __init__(self, deck_id):
        self.deck_id = deck_id


class CardNotFoundError(NotFoundError):
    def __init__(self, card_id):
        self.card_id = card_id
