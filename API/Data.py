from flask import Blueprint
from typing import Any
from Core import Core

api_data = Blueprint("api_data", __name__)

@api_data.route(rule="/example", methods=["POST"])
def exmaple() -> Any:
    pass