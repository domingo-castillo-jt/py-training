from src.infrastructure.persistance.item_api_v1_repository import ItemApiV1Repository


def get_one_item_use_case(id: int) -> dict:
    return dict(ItemApiV1Repository().get_one(id))
