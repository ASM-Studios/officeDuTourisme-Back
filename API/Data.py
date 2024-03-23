from flask import Blueprint, request, jsonify
from typing import Any
from Core import Core

api_data = Blueprint("api_data", __name__)

data = Core()

@api_data.route(rule="/getByCoordinates", methods=["GET"])
def getByCoordinates() -> Any:
    body: dict = request.get_json()
    if not body.get("coordinates"):
        return jsonify("Missing coordinates"), 400
    if not body["coordinates"].get("lat"):
        return jsonify("Missing lat in coordinates"), 400
    if not body["coordinates"].get("lng"):
        return jsonify("Missing lng in coordinates"), 400

    return data.getByCoord(body.get("coordinates"))
