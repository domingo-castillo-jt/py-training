from typing import List
from src.core.domain.entities.item import Item
from abc import ABCMeta, abstractmethod


class ItemRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self) -> List[Item]:
        raise NotImplementedError

    @abstractmethod
    def get_one(self,id:int) -> Item:
        raise NotImplementedError
