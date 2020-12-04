from .ABCTicket import ABCTicket


class Ticket(ABCTicket):
    _price_per_minute: int = 50
    _fees: int = 500
    _description = "Simple ticket"

    def __init__(self, time: int) -> None:
        self.time = time

    def get_price(self) -> float:
        return self.time * self._price_per_minute + self._fees
