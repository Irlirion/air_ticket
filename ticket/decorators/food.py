from .ABCDecorator import ABCDecorator


class Food(ABCDecorator):
    _price: int

    def get_price(self) -> float:
        return self._price + self.ticket.get_price()

    @property
    def description(self) -> str:
        return ", ".join([self.ticket.description, self._description])


class Combo1(Food):
    _price: int = 200
    _description = "Combo #1"


class Combo2(Food):
    _price: int = 300
    _description = "Combo #2"


class Combo3(Food):
    _price: int = 400
    _description = "Combo #3"
