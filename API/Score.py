from flask import blueprints, request
from typing import Any
import json

api_score = Blueprint("api_score", __name__)

scoreFilePath: str = 'score.json'

@api_score.route(rule="/setScoreByUser", methods=["POST"])
def setScoreByUser() -> Any:
    body: dict = request.get_json()
