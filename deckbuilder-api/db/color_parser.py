import re


def parse(mana_cost):
    cost = {"colorless": 0, "W": 0, "B": 0, "U": 0, "R": 0, "G": 0}
    costs = re.split(r"\}\{", mana_cost[1:-1])

    for c in costs:
        if re.match(r"\d+", mana_cost) is None:
            cost["colorless"] = cost["colorless"] + 1
        else:
            cost[c] = cost[c] + 1

    return cost
