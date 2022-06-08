import os
from src.core.domain.ports.item_repository import ItemRepository
from typing import List
from src.core.domain.entities.item import Item
import requests


class ItemDatasource(ItemRepository):
    def get_all(self) -> List[Item]:
        x = requests.get(
            "http://api.rollbar.com/api/1/items",
            headers={"X-Rollbar-Access-Token": os.environ.get("ROLLBAR_READ_TOKEN")},
        )
        return x.text

    def get_one(self, id: int) -> Item:
        x = requests.get(
            f"http://api.rollbar.com/api/1/item/{id}",
            headers={"X-Rollbar-Access-Token":os.environ.get("ROLLBAR_READ_TOKEN")},
        )
        return x.text

    def post(self, item:Item) -> Item:
        x = requests.post("http://api.rollbar.com/api/1/item/", data=item, headers={"X-Rollbar-Access-Token":os.environ.get("ROLLBAR_POST_SERVER_TOKEN")})
        return x.text

    def patch(self, id:int, item:Item) -> Item:
        x = requests.patch(
            f"http://api.rollbar.com/api/1/item/{id}",
            data=item,
            headers={"X-Rollbar-Access-Token": os.environ.get("ROLLBAR_WRITE_TOKEN")},
        )
        return x.text
