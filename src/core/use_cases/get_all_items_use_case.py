from src.infrastructure.persistance.item_api_v1_repository import ItemApiV1Repository
from typing import List
from src.core.domain.entities.item import Item

def get_all_items_use_case() -> List[Item]:
    return ItemApiV1Repository().get_all()
