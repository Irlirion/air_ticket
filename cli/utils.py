import json
from io import TextIOWrapper

from ticket import Ticket
from ticket.ABCTicket import ABCTicket
from ticket.decorators import class_type, Baggage, food, Transfer, Age


def create_ticket(time: int, cls_type: str, weight: int, age: int, food_type: str = None,
                  transfer: bool = False) -> ABCTicket:
    ticket: ABCTicket = Ticket(time=time)
    ticket = class_type.EconomyClass(ticket) if cls_type == 'economy' else class_type.BusinessClass(ticket)
    ticket = Baggage(ticket, weight)
    if food_type != 'nothing':
        if food_type == 'combo1':
            ticket = food.Combo1(ticket)
        elif food_type == 'combo2':
            ticket = food.Combo2(ticket)
        elif food_type == 'combo3':
            ticket = food.Combo3(ticket)
        else:
            raise ValueError(f"Food type {food_type} not found. Supporting types 'combo1', 'combo12,' combo3'")
    ticket = transfer and Transfer(ticket) or ticket
    ticket = Age(ticket, age)

    return ticket


def create_ticket_json(file: TextIOWrapper) -> ABCTicket:
    options = json.loads(file.read())
    ticket = create_ticket(**options)
    return ticket
