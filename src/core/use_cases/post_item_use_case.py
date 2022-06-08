from src.infrastructure.persistance.item_datasource import ItemDatasource
from src.core.domain.entities.item import Item

def post_item_use_case(id: int) -> Item:
    return ItemDatasource().post(id)

