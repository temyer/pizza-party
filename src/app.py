from typing import Callable
from random import randint
from functools import wraps

from src.pizza import Pizza


def log(*args):
    def dec(fn: Callable):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            fn(*args, **kwargs)

            seconds_taken = randint(1, 3)

            if not template:
                print(f'{fn.__name__} - {seconds_taken}c!')
            else:
                print(template.format(seconds_taken))

        return wrapper

    if len(args) == 1 and callable(args[0]):
        template = None
        return dec(args[0])
    else:
        template = args[0]
        return dec


@log
def bake(pizza: Pizza):
    """Готовит пиццу"""
    pass


@log('🛵 Доставили за {}c!')
def deliver(pizza: Pizza):
    """Доставляет пиццу"""
    pass


@log('🏠 Забрали за {}c!')
def pickup(pizza: Pizza):
    """Самовывоз"""
    pass
