from .ABCDecorator import ABCDecorator


class ABCClass(ABCDecorator):
    _factor: float

    def get_price(self) -> float:
        return self.ticket.get_price() * self._factor

    @property
    def description(self) -> str:
        return self._description


class BusinessClass(ABCClass):
    _factor = 1.5
    _description = "Business class"


class EconomyClass(ABCClass):
    _factor = 1
    _description = "Economy class"
