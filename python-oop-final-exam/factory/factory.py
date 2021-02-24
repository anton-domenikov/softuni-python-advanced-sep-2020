from abc import ABC, abstractmethod


class Factory(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}  # (name of the ingredient for key and quantity of the ingredient as a value)

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        # returns whether the given amount of product (value) can be added in the ingredients
        sum_ingredients = sum([v for k, v in self.ingredients.items()])
        return sum_ingredients + value <= self.capacity
