from project.factory.factory import Factory


class ChocolateFactory(Factory):
    PASSABLE_INGREDIENTS = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = {}  # (recipe name as key and dictionary of needed ingredients to make the recipe)
        self.products = {}  # (made recipes; recipe name as key and quantity as value)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.PASSABLE_INGREDIENTS:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {ChocolateFactory}")
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

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        try:
            recipe_ingredients = self.recipes[recipe_name]
            for ingr in recipe_ingredients:
                self.ingredients[ingr] -= recipe_ingredients[ingr]  # or maybe just -= 1 ???
            if recipe_name in self.products:
                self.products[recipe_name] += 1
            else:
                self.products[recipe_name] = 1
        except KeyError:
            raise TypeError("No such recipe")
