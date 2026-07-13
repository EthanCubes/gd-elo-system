from flask import Flask, jsonify, request
from flask_cors import CORS

import loop

app = Flask(__name__)
CORS(app)

@app.route("/api/search")
def search():
    name = request.args.get("name")
    playerData, rating = loop.userSearch(name)
    return jsonify(playerData, rating)