from src.infrastructure.persistance.item_datasource import ItemDatasource
from src.core.domain.entities.item import Item

def patch_item_use_case(id:int, item: Item) -> Item:
    return ItemDatasource().patch(id,item)

