from project.factory.factory import Factory


class PaintFactory(Factory):
    PASSABLE_INGREDIENTS = ["white", "yellow", "blue", "green", "red"]

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.PASSABLE_INGREDIENTS:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {PaintFactory}")
            # check if its the NAME of the CLASS or SELF.NAME ?????
        else:
            if self.can_add(quantity):
                # return true
                if ingredient_type in self.ingredients:
                    self.ingredients[ingredient_type] += quantity
                else:
                    self.ingredients[ingredient_type] = quantity
            else:
                # not enough space for ingredient
                raise ValueError("Not enough space in factory")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        try:
            quantity_of_our_ingredient = self.ingredients[ingredient_type]
            if self.ingredients[ingredient_type] - quantity < 0:
                raise ValueError("Ingredient quantity cannot be less than zero")
            else:
                self.ingredients[ingredient_type] -= quantity
        except KeyError:
            raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients
