from flask import Flask, request, jsonify
from flask_cors import CORS
from db.card_dao import CardDao
# from db.import_cards import import_cards

app = Flask(__name__)
CORS(app)
dao = CardDao()


@app.route('/cards')
def search_card():
    search = request.args.get("search")
    result = dao.search_cards(search)
    return jsonify(result)


def run():
    # import_cards()
    app.run()
