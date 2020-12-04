from .ABCDecorator import ABCDecorator
from ..ABCTicket import ABCTicket


class Baggage(ABCDecorator):
    _description = "weight of baggage"
    _base_price: int = 1000
    _threshold: int = 15
    _surcharge: int = 100

    def __init__(self, ticket: ABCTicket, weight: float) -> None:
        super().__init__(ticket)
        self.weight = weight

    def get_price(self) -> float:
        if self.weight <= 15:
            return self.ticket.get_price()
        return self._base_price + (self.weight - 15) * self._surcharge + self.ticket.get_price()

    @property
    def description(self) -> str:
        return ", ".join([self.ticket.description, self._description + ': ' + str(self.weight)])
