from src.mixins import IconMixin
from src.pizza import Ingredient, Margherita, Pizza, PizzaSize


def test_icon_mixin():
    class IconPizza(IconMixin, Margherita):
        pass

    ip = IconPizza()

    assert 'Margherita 🧀' in ip.dict()


def test_no_icon():
    class DummyPizza(Pizza):
        def __init__(self, size: PizzaSize = PizzaSize.L) -> None:
            self.name = 'DummyPizza'
            self.size = size
            self.recipe = [
                Ingredient.Mozzarella,
            ]

    class IconDummyPizza(IconMixin, DummyPizza):
        pass

    idp = IconDummyPizza()
    assert 'DummyPizza' in idp.dict()
