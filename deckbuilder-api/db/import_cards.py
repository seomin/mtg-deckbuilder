import json
import os
from db.card_dao import CardDao

dao = CardDao()
mci_base_url = "https://magiccards.info/scans/en/"


def import_cards():
    print("Dropping all cards...")
    dao.drop_cards()

    print("Loading cards from json file...")
    script_dir = os.path.dirname(__file__)
    rel_path = "../cards/AllSets-x.json"
    abs_file_path = os.path.join(script_dir, rel_path)
    file = open(abs_file_path, encoding="UTF-8")
    data = json.load(file)

    print("Saving cards in database...")
    for set_name, set_data in data.items():
        set_cards = set_data["cards"]
        mci_set = set_data.get("magicCardsInfoCode")

        for card in set_cards:
            # Only set mciUrl for cards whose set is available on MCI
            if mci_set is not None:
                mci_number = extract_mci_number(card)
                if mci_number is not None:
                    card["mciUrl"] = mci_base_url + mci_set + "/" + mci_number + ".jpg"

            dao.save_card(card)
    print("Done.")


def extract_mci_number(card):
    if "mciNumber" in card:
        return card["mciNumber"]

    if "number" in card:
        return card["number"]

    return None
