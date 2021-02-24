from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name, chocolate_factory, egg_factory, paint_factory):
        self.name = name
        self.storage = {}  # (product name as key and quantity of the product as value)
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory

    def add_chocolate_ingredient(self, type_i: str, quantity: int):
        self.chocolate_factory.add_ingredient(type_i, quantity)

    def add_egg_ingredient(self, type_i: str, quantity: int):
        self.egg_factory.add_ingredient(type_i, quantity)

    def add_paint_ingredient(self, type_i: str, quantity: int):
        self.paint_factory.add_ingredient(type_i, quantity)

    def make_chocolate(self, recipe: str):
        prev_products = sum([v for k, v in self.chocolate_factory.products.items()])
        self.chocolate_factory.make_chocolate(recipe)
        curr_products = sum([v for k, v in self.chocolate_factory.products.items()])
        if curr_products > prev_products:
            if recipe in self.storage:
                self.storage[recipe] += 1
            else:
                self.storage[recipe] = 1

    def paint_egg(self, color: str, egg_type: str):
        try:
            egg = self.egg_factory.ingredients[egg_type]
            paint = self.paint_factory.ingredients[color]
            self.egg_factory.ingredients[egg_type] -= 1
            self.paint_factory.ingredients[color] -= 1
            curr_egg = f'{color} {egg_type}'
            if curr_egg in self.storage:
                self.storage[curr_egg] += 1
            else:
                self.storage[curr_egg] = 1
        except KeyError:
            raise ValueError("Invalid commands")

    def __repr__(self):
        result = []
        result.append(f'Shop name: {self.name}')
        result.append('Shop Storage:')
        for key in self.storage.keys():
            result.append(f'{key}: {self.storage[key]}')

        return '\n'.join(result)
