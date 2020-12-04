from abc import ABC, abstractmethod

from ticket.ABCTicket import ABCTicket


class ABCDecorator(ABCTicket, ABC):

    def __init__(self, ticket: ABCTicket) -> None:
        self.ticket = ticket

    @property
    @abstractmethod
    def description(self) -> str:
        pass
