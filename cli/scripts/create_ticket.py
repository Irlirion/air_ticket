from io import TextIOWrapper

import click

from cli.utils import create_ticket, create_ticket_json


@click.command()
@click.option('--time', prompt="Time of fly", type=click.IntRange(min=0),
              help="Time of flying in minutes. Default price = 50 rub/min.")
@click.option('--cls_type', prompt="Class", default='economy', type=click.Choice(['business', 'economy']),
              help="Type of ticket. Default factor for Business class is 1.5.")
@click.option('--weight', prompt="Weight of baggage", default=0, type=click.IntRange(min=0),
              help="Weight of baggage. Weight <= 15 is free. If the weight > 15 then price + 1000 rub + 100 rub for "
                   "each kg over 15.")
@click.option('--age', prompt="Age", type=click.IntRange(min=0),
              help="Age of passenger. If the age <= 12, there will be a 30% discount.")
@click.option('--food_type', prompt="Combo type", default='nothing',
              type=click.Choice(['1', '2', '3', 'nothing']),
              help="Type of food. Price: Combo #1: 200 rub, Combo #2: 300 rub, Combo #3: 400 rub.")
@click.option('--transfer', prompt="Transfer", default='No', type=bool,
              help="Does the passenger need a transfer? Price is 1000 rub.")
def get_ticket(time: int, cls_type: str, weight: int, age: int, food_type: str = None,
               transfer: bool = False) -> None:
    """
    CLI for creating air ticket.
    """
    ticket = create_ticket(time, cls_type, weight, age, food_type,
                           transfer)

    click.echo(f"Ticket: {ticket.description}")
    click.echo(f"Price: {round(ticket.get_price(), 2)}")


@click.command()
@click.option('-e', '--echo', default=True, type=bool, help="Echo price and description to console.")
@click.argument('input_json', type=click.File('r'))
@click.argument('output_json', type=click.File('w'))
def get_ticket_json(input_json: TextIOWrapper, output_json: TextIOWrapper, echo: bool) -> None:
    """
    Read INPUT_JSON and write ticket cost in OUTPUT_JSON
    """
    ticket = create_ticket_json(input_json)

    if echo:
        click.echo(f"Ticket: {ticket.description}")
        click.echo(f"Price: {round(ticket.get_price(), 2)}")

    json = '{"cost": ' + f'{round(ticket.get_price(), 2)}' + '}\n'
    output_json.write(json)
