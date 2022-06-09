from abc import ABCMeta, abstractmethod
from typing import List

from src.core.domain.dto.patch_info_dto import PatchInfo
from src.core.domain.entities.item import Item


class ItemRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self) -> List[Item]:
        raise NotImplementedError

    @abstractmethod
    def get_one(self, id: int) -> Item:
        raise NotImplementedError

    @abstractmethod
    def post(self, item: dict) -> Item:
        raise NotImplementedError

    @abstractmethod
    def patch(self, id: int, item: PatchInfo) -> PatchInfo:
        raise NotImplementedError
