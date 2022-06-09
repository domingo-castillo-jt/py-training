from pydantic_factories import ModelFactory

from src.core.domain.dto.patch_info_dto import PatchInfo
from src.core.domain.entities.item import Item


class ItemFactory(ModelFactory):
    __model__ = Item

class PatchInfoFactory(ModelFactory):
    __model__ = PatchInfo
