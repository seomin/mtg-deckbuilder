import json
import os
from db.card_dao import CardDao

dao = CardDao()
mci_base_url = "https://magiccards.info/scans/en/"


def import_cards():
    dao.drop_cards()

    # Load cards from json file
    script_dir = os.path.dirname(__file__)
    rel_path = "../cards/AllSets-x.json"
    abs_file_path = os.path.join(script_dir, rel_path)
    file = open(abs_file_path, encoding="UTF-8")
    data = json.load(file)

    # Save cards in database
    for set_name, set_data in data.items():
        set_cards = set_data["cards"]
        mci_set = set_data.get("magicCardsInfoCode", set_name.lower())

        # TODO import cards even if they do not have number or mciNumber
        for card in set_cards:
            if "mciNumber" not in card:
                if "number" not in card:
                    print("Card \"" + card["name"] + "\" in set " + set_name + " has neither number nor mciNumber. Ignoring...")
                    continue
                mci_number = card["number"]
            else:
                mci_number = card["mciNumber"]

            card["mciUrl"] = mci_base_url + mci_set + "/" + mci_number + ".jpg"
            dao.save_card(card)
