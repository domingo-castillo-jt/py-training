from src.infrastructure.persistance.item_api_v1_repository import ItemApiV1Repository


def patch_item_use_case(id: int, item: dict) -> dict:
    return ItemApiV1Repository().patch(id, item)
