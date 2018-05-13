class CardEntity:
    def __init__(self, _id, _name, _mci_url, _cmc, _manaCost, _tags=None):
        self.id = _id
        self.name = _name
        self.mciUrl = _mci_url
        self.cmc = _cmc
        self.manaCost = _manaCost

        if _tags is None:
            self.tags = []
        else:
            self.tags = _tags