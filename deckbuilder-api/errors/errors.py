class Error(Exception):
    """Base class for errors"""
    def __init__(self, _message, _status_code):
        self.message = _message
        self.status_code = _status_code


class NotFoundError(Error):
    """Some requested entity was not found"""
    def __init__(self, _message):
        super().__init__(_message, 404)


class DeckNotFoundError(NotFoundError):
    def __init__(self, deck_id):
        super().__init__("Could not find deck with id " + deck_id)


class CardNotFoundError(NotFoundError):
    def __init__(self, card_id):
        super().__init__("Could not find card with id " + card_id)
