from src.infrastructure.persistance.item_datasource import ItemDatasource
from src.core.domain.entities.item import Item

def get_one_item_use_case() -> Item:
    return ItemDatasource().get_one()
