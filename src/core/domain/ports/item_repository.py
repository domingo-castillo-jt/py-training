from abc import ABCMeta, abstractmethod
from typing import List

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
    def patch(self, id: int, item: dict) -> dict:
        raise NotImplementedError
