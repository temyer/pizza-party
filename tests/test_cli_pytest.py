import random
from click.testing import CliRunner

from src.cli import menu, order


def test_menu():
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.output == \
        ("- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n"
            "- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n"
            "- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n")


def test_wrong_pizza_order():
    runner = CliRunner()
    result = runner.invoke(order, ['not_pepperoni'])

    assert result.output == "К сожалению, такой пиццы нет!\n"


def test_order_pickup():
    random.seed(0)
    runner = CliRunner()
    result = runner.invoke(order, ['pepperoni'])

    assert result.output == ("bake - 2c!\n"
                             "🏠 Забрали за 2c!\n")


def test_order_delivery():
    random.seed(0)
    runner = CliRunner()
    result = runner.invoke(order, ['pepperoni', '--delivery'])

    assert result.output == ("bake - 2c!\n"
                             "🛵 Доставили за 2c!\n")
