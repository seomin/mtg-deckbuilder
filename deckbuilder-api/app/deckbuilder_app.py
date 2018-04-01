from flask import Flask, request, jsonify
from flask_cors import CORS
from db.card_dao import CardDao
import uuid
# from db.import_cards import import_cards

app = Flask(__name__)
CORS(app)
dao = CardDao("deckbuilder_db")


@app.route('/cards')
def search_card():
    search = request.args.get("search")
    result = dao.search_cards(search)
    return jsonify(result)


@app.route('/deck', methods=['POST'])
def deck():
    _id = uuid.uuid4()
    name = request.args.get("name")
    dao.create_deck(_id, name)
    return _id


@app.route('/deck/<deck_id>')
def get_deck(deck_id):
    _deck = dao.get_deck(deck_id)
    return jsonify(_deck)


@app.route('deck/<deck_id>/card', methods=['POST'])
def add_card_to_deck(deck_id):
    card_id = request.form["card_id"]
    dao.add_card(deck_id, card_id)


def run():
    # import_cards()
    app.run()

