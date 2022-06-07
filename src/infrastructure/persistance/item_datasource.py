from src.core.domain.ports.item_repository import ItemRepository
from typing import List
from src.core.domain.entities.item import Item
import requests


class ItemDatasource(ItemRepository):
    def get_all(self) -> List[Item]:
        x = requests.get(
            "http://api.rollbar.com/api/1/items",
            headers={"X-Rollbar-Access-Token": "29b05bd130e14b27822d17787597ce72"},
        )
        return x.text

    def get_one(self, id: int) -> Item:
        x = requests.get(
            f"http://api.rollbar.com/api/1/item/{id}",
            headers={"X-Rollbar-Access-Token": "29b05bd130e14b27822d17787597ce72"},
        )
        return x.text