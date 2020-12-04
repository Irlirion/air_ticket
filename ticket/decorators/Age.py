from .ABCDecorator import ABCDecorator
from ..ABCTicket import ABCTicket


class Age(ABCDecorator):
    _description: str = 'age'

    def __init__(self, ticket: ABCTicket, age: int) -> None:
        super().__init__(ticket)
        self.age = age

    def get_price(self) -> float:
        if self.age <= 12:
            return self.ticket.get_price() * 0.7
        return self.ticket.get_price()

    @property
    def description(self) -> str:
        return ", ".join([self.ticket.description, self._description + ': ' + str(self.age)])
