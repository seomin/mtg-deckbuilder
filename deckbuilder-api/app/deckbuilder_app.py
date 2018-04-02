from flask import Flask, request, jsonify
from flask_cors import CORS
from db.card_dao import CardDao
# from db.import_cards import import_cards
from errors.errors import DeckNotFoundError

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
    name = request.args.get("name")
    deck_id = dao.create_deck(name)
    return deck_id


@app.route('/deck')
def get_decks():
    _decks = dao.get_decks()
    return jsonify(_decks)


@app.route('/deck/<deck_id>')
def get_deck(deck_id):
    try:
        _deck = dao.get_deck(deck_id)
    except DeckNotFoundError as e:
        return "Could not find deck with id " + e.deck_id, 404
    return jsonify(_deck)


@app.route('/deck/<deck_id>', methods=['DELETE'])
def delete_deck(deck_id):
    # TODO handle case if deck is not found
    dao.delete_deck(deck_id)


@app.route('/deck/<deck_id>/card', methods=['POST'])
def add_card_to_deck(deck_id):
    # TODO handle case if card is not found
    card_id = request.form["card_id"]
    dao.add_card(deck_id, card_id)


@app.route('/deck/<deck_id>/card/<card_id>', methods=['DELETE'])
def delete_card_from_deck(deck_id, card_id):
    # TODO handle case if card is not found
    deck_id = request.form["deck_id"]
    card_id = request.form["card_id"]
    dao.delete_card_from_deck(deck_id, card_id)


def run():
    # import_cards()
    app.run()

