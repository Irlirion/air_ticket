from io import TextIOWrapper

import click

from cli.utils import create_ticket, create_ticket_json


@click.command()
@click.option('--time', prompt="Time of fly", type=click.IntRange(min=0))
@click.option('--cls_type', prompt="Class", default='economy', type=click.Choice(['business', 'economy']))
@click.option('--weight', prompt="Weight of baggage", default=0, type=click.IntRange(min=0))
@click.option('--age', prompt="Age", type=click.IntRange(min=0))
@click.option('--food_type', prompt="Combo type", default='nothing',
              type=click.Choice(['combo1', 'combo2', 'combo3', 'nothing']))
@click.option('--transfer', prompt="Transfer", default='No', type=bool)
def get_ticket(time: int, cls_type: str, weight: int, age: int, food_type: str = None,
               transfer: bool = False) -> None:
    ticket = create_ticket(time, cls_type, weight, age, food_type,
                           transfer)

    click.echo(f"Ticket: {ticket.description}")
    click.echo(f"Price: {round(ticket.get_price(), 2)}")


@click.command()
@click.option('-e', '--echo', default=True, type=bool)
@click.argument('file', type=click.File('r'))
@click.argument('out', type=click.File('w'))
def get_ticket_json(file: TextIOWrapper, out: TextIOWrapper, echo: bool) -> None:
    ticket = create_ticket_json(file)

    if echo:
        click.echo(f"Ticket: {ticket.description}")
        click.echo(f"Price: {round(ticket.get_price(), 2)}")

    json = '{"cost": ' + f'{round(ticket.get_price(), 2)}' + '}\n'
    out.write(json)
