from flask import Blueprint, request

from src.core.use_cases.get_all_items_use_case import get_all_items_use_case
from src.core.use_cases.get_one_item_use_case import get_one_item_use_case
from src.core.use_cases.patch_item_use_case import patch_item_use_case
from src.core.use_cases.post_item_use_case import post_item_use_case

api = Blueprint("api", __name__)


@api.route("/")
def hello_world() -> str:
    return "Hello, World!"


@api.route("/items")
def get_items() -> dict:
    return get_all_items_use_case()


@api.route("/items/<int:id>")
def get_item(id: int) -> dict:
    return get_one_item_use_case(id)


@api.route("/items", methods=["POST"])
def post_item() -> dict:
    return post_item_use_case(dict(request.json if request.json else {}))


@api.route("/items/<int:id>", methods=["PUT", "PATCH"])
def patch_item(id: int) -> dict:
    return patch_item_use_case(id, dict(request.json if request.json else {}))
