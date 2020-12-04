from abc import ABC, abstractmethod


class ABCTicket(ABC):
    _description: str = "Unknown ticket"

    @property
    def description(self) -> str:
        return self._description

    @abstractmethod
    def get_price(self) -> float:
        pass
