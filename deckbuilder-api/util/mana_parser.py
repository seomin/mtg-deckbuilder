import re


def parse(mana_string):
    mana = {"colorless": 0, "W": 0, "B": 0, "U": 0, "R": 0, "G": 0}
    costs = re.split(r"\}\{", mana_string[1:-1])

    for c in costs:
        if re.match(r"\d+", c) is None:
            mana[c] = mana[c] + 1
        else:
            mana["colorless"] = mana["colorless"] + int(c)

    return mana
