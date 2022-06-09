from src.core.domain.DTOs.patch_dto import PatchInfo
from src.infrastructure.persistance.item_api_v1_repository import ItemApiV1Repository


def patch_item_use_case(id: int, patch_info: PatchInfo) -> dict:
    return dict(ItemApiV1Repository().patch(id, patch_info))
