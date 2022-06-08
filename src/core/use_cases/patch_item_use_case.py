from src.infrastructure.persistance.item_api_v1_repository import ItemApiV1Repository
from src.core.domain.entities.item import Item

def patch_item_use_case(id:int, item: Item) -> Item:
    return ItemApiV1Repository().patch(id,item)

