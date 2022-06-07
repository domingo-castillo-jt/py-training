from flask import Blueprint
import requests
from src.core.use_cases.get_all_items_use_case import get_all_items_use_case
from src.core.use_cases.get_one_item_use_case import get_one_item_use_case

api = Blueprint('api', __name__)
                   

@api.route("/")
def hello_world() -> str:
    return "Hello, World!"
    
@api.route("/items")
def get_items() -> str:
    return get_all_items_use_case()


@api.route("/items/<int:id>")
def get_item(id: int) -> str:
    return get_one_item_use_case(id)


@api.route('/items', methods=['POST'])
def post_item()-> str:
    x = requests.post("http://api.rollbar.com/api/1/item/", data=request.data, headers={"X-Rollbar-Access-Token":os.environ.get("ROLLBAR_POST_SERVER_TOKEN")})
    return x.text


@api.route("/items/<int:id>", methods=["PUT", "PATCH"])
def put_item(id: int) -> str:
    x = requests.patch(
        f"http://api.rollbar.com/api/1/item/{id}",
        data=request.data,
        headers={"X-Rollbar-Access-Token": os.environ.get("ROLLBAR_WRITE_TOKEN")},
    )
    return x.text
