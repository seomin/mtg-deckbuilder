class DeckEntity:
    def __init__(self, _id, _name):
        self.name = _name
        self.id = _id
        self.cards = list()
        self.cmcDistribution = dict()
        self.manaDistribution = {"colorless": 0, "W": 0, "B": 0, "U": 0, "R": 0, "G": 0}

    def add_card(self, new_card):
        self.cards.append(new_card)

