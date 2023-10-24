from abc import ABC, abstractmethod
import IGameItem


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self) -> IGameItem:
        pass
