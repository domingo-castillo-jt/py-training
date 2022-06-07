from src.infrastructure.persistance.item_datasource import ItemDatasource
from typing import List
from src.core.domain.entities.item import Item

def get_all_items_use_case() -> List[Item]:
    return ItemDatasource().get_all()

if __name__ == "__main__":
    print(get_all_items_use_case())
