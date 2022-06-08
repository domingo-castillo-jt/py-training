import json
import os
from typing import List

import requests

from src.core.domain.entities.item import Item
from src.core.domain.ports.item_repository import ItemRepository


class ItemApiV1Repository(ItemRepository):
    # def _rollbar_request(url:str, method, token)

    def get_all(self) -> List[Item]:
        response = requests.get(
            "http://api.rollbar.com/api/1/items",
            headers={
                "X-Rollbar-Access-Token": os.environ.get("ROLLBAR_READ_TOKEN", "")
            },
        )
        return list(map(lambda item: Item(**item), response.json()["result"]["items"]))

    def get_one(self, id: int) -> Item:
        response = requests.get(
            f"http://api.rollbar.com/api/1/item/{id}",
            headers={
                "X-Rollbar-Access-Token": os.environ.get("ROLLBAR_READ_TOKEN", "")
            },
        )
        return Item(**response.json()["result"])

    def post(self, item: dict) -> Item:
        response = requests.post(
            "http://api.rollbar.com/api/1/item/",
            data=json.dumps(item),
            headers={
                "X-Rollbar-Access-Token": os.environ.get(
                    "ROLLBAR_POST_SERVER_TOKEN", ""
                )
            },
        )
        return Item(**response.json()["result"])

    def patch(self, id: int, item: dict) -> dict:
        response = requests.patch(
            f"http://api.rollbar.com/api/1/item/{id}",
            data=json.dumps(item),
            headers={
                "X-Rollbar-Access-Token": os.environ.get("ROLLBAR_WRITE_TOKEN", "")
            },
        )
        return dict(response.json()["result"])
