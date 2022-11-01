from typing import List, Type
import pytest

from src.pizza import Pizza, Margherita, Pepperoni, Hawaiian, Ingredient, \
    PizzaSize


def test_forbid_pizza_class_creation():
    with pytest.raises(TypeError):
        Pizza()


@pytest.mark.parametrize(
    'cls, ingredients', [
        (Margherita, [
                Ingredient.TomatoSauce,
                Ingredient.Mozzarella,
                Ingredient.Tomatoes,
        ]),
        (Pepperoni, [
                Ingredient.TomatoSauce,
                Ingredient.Mozzarella,
                Ingredient.Pepperoni,
        ]),
        (Hawaiian, [
                Ingredient.TomatoSauce,
                Ingredient.Mozzarella,
                Ingredient.Chicken,
                Ingredient.Pineapples,
        ]),
    ]
)
def test_pizza_content(cls: Type[Pizza], ingredients: List[Ingredient]):
    p = cls()

    assert ingredients == p.recipe


def test_dict():
    m = Margherita()

    recipe = [
        Ingredient.TomatoSauce,
        Ingredient.Mozzarella,
        Ingredient.Tomatoes,
    ]

    assert {'Margherita': recipe} == m.dict()


def test_default_size():
    m1 = Margherita(PizzaSize.L)
    m2 = Margherita()

    assert m1 == m2


def test_pizza_equity():
    m1 = Margherita(PizzaSize.XL)
    p1 = Pepperoni(PizzaSize.XL)

    assert m1 != p1
