from src.infrastructure.persistance.item_api_v1_repository import ItemApiV1Repository


def get_all_items_use_case() -> dict:
    return {"items": [dict(item) for item in ItemApiV1Repository().get_all()]}
