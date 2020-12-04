from ticket.decorators.ABCDecorator import ABCDecorator


class Transfer(ABCDecorator):
    _price = 1000
    _description = "transfer"

    def get_price(self) -> float:
        return self._price + self.ticket.get_price()

    @property
    def description(self) -> str:
        return ", ".join([self.ticket.description, self._description + ': ' + str(self._price)])
