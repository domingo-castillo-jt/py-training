from src.infrastructure.persistance.item_api_v1_repository import ItemApiV1Repository


def post_item_use_case(item: dict) -> dict:
    return dict(ItemApiV1Repository().post(item))
