import random

from src.app import bake, deliver, pickup, log
from src.pizza import Margherita


def test_dummy_functions():
    m = Margherita()

    assert bake.__wrapped__(m) is None
    assert deliver.__wrapped__(m) is None
    assert pickup.__wrapped__(m) is None


def test_log(capsys):
    random.seed(0)
    decorated_log = log(bake.__wrapped__)

    decorated_log(Margherita())
    out, _ = capsys.readouterr()

    assert 'bake - 2c!\n' == out


def test_parametrized_log(capsys):
    random.seed(0)
    template = 'Delivered in {} secs!'

    decorated_log = log(template)(deliver.__wrapped__)

    decorated_log(Margherita())
    out, _ = capsys.readouterr()

    assert 'Delivered in 2 secs!\n' == out
