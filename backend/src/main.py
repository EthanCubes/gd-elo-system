from flask import Flask, jsonify, request
from flask_cors import CORS

from .loop import userSearch

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/api/search")
    def search():
        name = request.args.get("name")
        playerData, rating = userSearch(name)
        return jsonify(playerData, rating)
    
    return app