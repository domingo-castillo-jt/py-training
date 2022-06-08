from src.infrastructure.persistance.item_api_v1_repository import ItemApiV1Repository
from src.core.domain.entities.item import Item

def get_one_item_use_case(id: int) -> Item:
    return ItemApiV1Repository().get_one(id)

