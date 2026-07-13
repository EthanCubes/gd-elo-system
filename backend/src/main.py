from flask import Flask, jsonify, request
from flask_cors import CORS

from .loop import userSearch

app = Flask(__name__)
CORS(app)

@app.route("/api/search")
def search():
    name = request.args.get("name")
    playerData, rating = userSearch(name)
    return jsonify(playerData, rating)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)