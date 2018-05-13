import re


def parse(mana_string):
    mana = {"colorless": 0, "W": 0, "B": 0, "U": 0, "R": 0, "G": 0}
    costs = re.split(r"\}\{", mana_string[1:-1])

    for c in costs:
        if re.match(r"\d+", c) is not None:
            mana["colorless"] = mana["colorless"] + int(c)
        elif re.match(r"W|B|U|R|G", c) is not None:
            mana[c] = mana[c] + 1

    return mana
