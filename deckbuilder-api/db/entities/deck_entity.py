class DeckEntity:
    def __init__(self, _id, _name):
        self.name = _name
        self.id = _id
        self.cards = list()
        self.cmc_distribution = dict()

    def add_card(self, new_card):
        self.cards.append(new_card)

