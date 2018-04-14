from flask import Flask, request, jsonify
from flask_cors import CORS

from db.card_dao import CardDao
# from db.import_cards import import_cards
from errors.errors import Error

app = Flask(__name__)
CORS(app)
dao = CardDao("deckbuilder_db")


@app.route('/cards')
def search_card():
    search = request.args.get("search")
    result = dao.search_cards(search)
    return jsonify(result)


@app.route('/deck', methods=['POST'])
def create_deck():
    name = request.form["name"]
    deck_id = dao.create_deck(name)
    return jsonify(deck_id)


@app.route('/deck')
def get_decks():
    _decks = dao.get_decks()
    return jsonify(_decks)


@app.route('/deck/<deck_id>')
def get_deck(deck_id):
    try:
        _deck = dao.get_deck(deck_id)
    except Error as e:
        return e.message, e.status_code
    return jsonify(_deck)


@app.route('/deck/<deck_id>', methods=['DELETE'])
def delete_deck(deck_id):
    try:
        _deck = dao.delete_deck(deck_id)
    except Error as e:
        return e.message, e.status_code
    return jsonify(_deck)


@app.route('/deck/<deck_id>/card', methods=['POST'])
def add_card_to_deck(deck_id):
    card_id = request.form["card_id"]
    try:
        dao.add_card_to_deck(deck_id, card_id)
    except Error as e:
        return e.message, e.status_code
    return card_id


@app.route('/deck/<deck_id>/card/<card_id>', methods=['DELETE'])
def delete_card_from_deck(deck_id, card_id):
    try:
        dao.delete_card_from_deck(deck_id, card_id)
    except Error as e:
        return e.message, e.status_code
    return card_id


def run():
    # dao.drop_db()
    # import_cards("AllSets-x.json", dao)
    app.run()

