from typing import Dict, List

from src.pizza import Ingredient


class IconMixin:
    __ICONS = {
        'Margherita': '🧀',
        'Pepperoni': '🍕',
        'Hawaiian': '🍍',
    }

    def dict(self) -> Dict[str, List[Ingredient]]:
        dict_repr = super().dict()  # type: ignore
        replaced_dict_repr = {}

        for name, recipe in dict_repr.items():
            if name in self.__ICONS:
                new_name = name + ' ' + self.__ICONS[name]
                replaced_dict_repr[new_name] = recipe
            else:
                replaced_dict_repr[name] = recipe

        return replaced_dict_repr
