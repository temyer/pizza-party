import abc
from typing import List, Dict
from enum import Enum


class PizzaSize(str, Enum):
    L = 'L'
    XL = 'XL'


class Ingredient(str, Enum):
    TomatoSauce = 'tomato sauce'
    Mozzarella = 'mozzarella'
    Tomatoes = 'tomatoes'
    Pepperoni = 'pepperoni'
    Chicken = 'chicken'
    Pineapples = 'pineapples'


class Pizza(abc.ABC):
    name: str
    size: PizzaSize
    recipe: List[Ingredient]

    @abc.abstractmethod
    def __init__(self, size: PizzaSize = PizzaSize.L) -> None:
        pass

    def dict(self) -> Dict[str, List[Ingredient]]:
        return {self.name: self.recipe}

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.size == o.size and self.recipe == o.recipe

        return False


class Margherita(Pizza):
    def __init__(self, size: PizzaSize = PizzaSize.L) -> None:
        self.name = 'Margherita'
        self.size = size
        self.recipe = [
            Ingredient.TomatoSauce,
            Ingredient.Mozzarella,
            Ingredient.Tomatoes,
        ]


class Pepperoni(Pizza):
    def __init__(self, size: PizzaSize = PizzaSize.L) -> None:
        self.name = 'Pepperoni'
        self.size = size
        self.recipe = [
            Ingredient.TomatoSauce,
            Ingredient.Mozzarella,
            Ingredient.Pepperoni,
        ]


class Hawaiian(Pizza):
    def __init__(self, size: PizzaSize = PizzaSize.L) -> None:
        self.name = 'Hawaiian'
        self.size = size
        self.recipe = [
            Ingredient.TomatoSauce,
            Ingredient.Mozzarella,
            Ingredient.Chicken,
            Ingredient.Pineapples,
        ]
