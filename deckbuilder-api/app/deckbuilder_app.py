from flask import Flask, request, jsonify
from flask_cors import CORS

# from db.import_cards import import_cards
from db.operations.operations_factory import OperationsFactory
from errors.errors import Error

DB_NAME = "deckbuilder_db"

app = Flask(__name__)
CORS(app)
operations_factory = OperationsFactory(DB_NAME)
card_operations = operations_factory.card_operations
deck_operations = operations_factory.deck_operations
playtest_operations = operations_factory.playtest_operations


@app.route('/cards')
def search_card():
    search = request.args.get("search")
    result = card_operations.search_cards(search)
    return jsonify(result)


# Deck routes
@app.route('/deck', methods=['POST'])
def create_deck():
    name = request.form["name"]
    deck_id = deck_operations.create_deck(name)
    return jsonify(deck_id)


@app.route('/deck')
def get_decks():
    _decks = deck_operations.get_decks()
    return jsonify(_decks)


@app.route('/deck/<deck_id>')
def get_deck(deck_id):
    try:
        _deck = deck_operations.get_deck(deck_id)
    except Error as e:
        return e.message, e.status_code
    return jsonify(_deck)


@app.route('/deck/<deck_id>', methods=['DELETE'])
def delete_deck(deck_id):
    try:
        _deck = deck_operations.delete_deck(deck_id)
    except Error as e:
        return e.message, e.status_code
    return jsonify(_deck)


@app.route('/deck/<deck_id>/card/<card_id>', methods=['GET'])
def get_card_from_deck(deck_id, card_id):
    try:
        result = deck_operations.get_card_from_deck(deck_id, card_id)
    except Error as e:
        return e.message, e.status_code
    return jsonify(result)


@app.route('/deck/<deck_id>/card', methods=['POST'])
def add_card_to_deck(deck_id):
    card_id = request.form["card_id"]
    try:
        deck_operations.add_card_to_deck(deck_id, card_id)
    except Error as e:
        return e.message, e.status_code
    return card_id


@app.route('/deck/<deck_id>/card/<card_id>', methods=['DELETE'])
def delete_card_from_deck(deck_id, card_id):
    try:
        deck_operations.delete_card_from_deck(deck_id, card_id)
    except Error as e:
        return e.message, e.status_code
    return card_id


@app.route('/deck/<deck_id>/card/<card_id>/tags', methods=['POST'])
def add_tags_to_card(deck_id, card_id):
    tags = request.form["tags"]
    try:
        deck_operations.add_tags_to_card(deck_id, card_id, tags)
    except Error as e:
        return e.message, e.status_code
    return card_id


@app.route('/deck/<deck_id>/card/<card_id>/tags', methods=['DELETE'])
def delete_tags_from_card(deck_id, card_id):
    tags = request.form["tags"]
    try:
        deck_operations.delete_tags_from_card(deck_id, card_id, tags)
    except Error as e:
        return e.message, e.status_code
    return card_id


# Playtesting routes
@app.route('/playtest/<deck_id>/move_card/from_zone')
def move_cards_between_zones(deck_id):
    from_zone = request.form["from_zone"]
    to_zone = request.form["to_zone"]
    number_of_cards = request.form["number_of_cards"]
    try:
        count = playtest_operations.move_cards_between_zones(deck_id, from_zone, to_zone, number_of_cards)
    except Error as e:
        return e.message, e.status_code
    return count


@app.route('/playtest/<deck_id>/move_card/card')
def move_card_to_zone(deck_id):
    card_id = request.form["card_id"]
    to_zone = request.form["to_zone"]
    try:
        count = playtest_operations.move_card_to_zone(deck_id, card_id, to_zone)
    except Error as e:
        return e.message, e.status_code
    return count


@app.route('/playtest/<deck_id>/shuffle')
def shuffle(deck_id):
    zone = request.form["zone"]
    try:
        count = playtest_operations.shuffle(deck_id, zone)
    except Error as e:
        return e.message, e.status_code
    return count


@app.route('/playtest/<deck_id>/reveal')
def reveal(deck_id):
    zone = request.form["zone"]
    number_of_cards = request.form["number_of_cards"]
    try:
        playtest_operations.reveal(deck_id, zone, number_of_cards)
    except Error as e:
        return e.message, e.status_code
    return


def run():
    # import_cards("AllSets-x.json", card_operations)
    app.run()

