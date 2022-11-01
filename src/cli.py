from typing import Dict, List, Type
import click

from src.pizza import Pizza, Margherita, Pepperoni, Hawaiian
from src.app import bake, deliver, pickup
from src.mixins import IconMixin


class CliMargherita(IconMixin, Margherita):
    pass


class CliPepperoni(IconMixin, Pepperoni):
    pass


class CliHawaiian(IconMixin, Hawaiian):
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza_mapper: Dict[str, Type[Pizza]] = {
        'margherita': Margherita,
        'pepperoni': Pepperoni,
        'hawaiian': Hawaiian,
    }

    if pizza not in pizza_mapper:
        return print('К сожалению, такой пиццы нет!')

    ordered_pizza = pizza_mapper[pizza]()

    bake(ordered_pizza)
    if delivery:
        deliver(ordered_pizza)
    else:
        pickup(ordered_pizza)


@cli.command()
def menu():
    """ Вывод меню """
    pizza_in_menu: List[Pizza] = [
        CliMargherita(),
        CliPepperoni(),
        CliHawaiian(),
    ]

    for pizza in pizza_in_menu:
        for name, recipe in pizza.dict().items():
            print(f'- {name}:', ', '.join(recipe))


if __name__ == '__main__':
    cli()
