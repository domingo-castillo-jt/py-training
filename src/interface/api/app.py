from src.core.use_cases.get_all_items_use_case import get_all_items_use_case
from src.core.use_cases.get_one_item_use_case import get_one_item_use_case
from flask import Flask, request
from typing import List
from src.core.domain.entities.item import Item

app = Flask(__name__)

import os
import rollbar  # type: ignore
import rollbar.contrib.flask  # type: ignore
from flask import got_request_exception
import requests

write_token = "6408eab7199940528fd17e193b7c7f5e"


@app.before_first_request
def init_rollbar() -> None:
    """init rollbar module"""
    rollbar.init(
        # access token
        "3c4fed617abb463caab073397f26507a",
        # environment name
        "production",
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False,
    )

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


@app.route("/")
def hello_world() -> str:
    return "Hello, World!"


@app.route("/items")
def get_items() -> str:
    x = requests.get(
        "http://api.rollbar.com/api/1/items",
        headers={"X-Rollbar-Access-Token": "29b05bd130e14b27822d17787597ce72"},
    )
    return x.text


@app.route("/items/<int:id>")
def get_item(id: int) -> str:
    return get_one_item_use_case()



@app.route("/items", methods=["POST"])
def post_item() -> List[Item]:
    return get_all_items_use_case()


@app.route("/items/<int:id>", methods=["PUT", "PATCH"])
def put_item(id: int) -> str:
    x = requests.patch(
        f"http://api.rollbar.com/api/1/item/{id}",
        data=request.data,
        headers={"X-Rollbar-Access-Token": "6408eab7199940528fd17e193b7c7f5e"},
    )
    return x.text


@app.route("/items/all")
def get_all_items_test() -> str:
    return get_all_items_use_case()
