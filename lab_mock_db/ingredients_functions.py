from abc import ABC, abstractmethod
import sys

ingredients = []


def add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type) -> None:
    ingredients.append(Ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type))


def find_all():
    """
    Find all ingredinets in List.
    :return: List of Ingredients
    """
    return ingredients.copy()


def find_by_name(name: str):
    """
    Find all ingredients by name
    :param name: name 'like'
    :return: List of Ingredients
    """
    copy = find_all()
    result = []

    for ingredient in copy:
        if name.casefold() in ingredient.name.casefold():
            result.append(ingredient)
    return result


class Ingredient:
    def __init__(self, name, calories, protein, fat, carbs, fiber, ingredient_type):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.fiber = fiber
        self.ingredient_type = ingredient_type

    def __str__(self):
        return str(self.__dict__)


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass


class ListIngredients(Strategy):
    def execute(self):
        all_ingredients = find_all()
        for i in all_ingredients:
            print(i)


class ListIngredientsByName(Strategy):
    def execute(self):
        ingredient_name = input("Podaj nazwę składnika: ")
        result = find_by_name(ingredient_name)
        for i in result:
            print(i)


class AddNewIngredient(Strategy):
    def execute(self):
        print("Dodawanie nowego składnika")
        name = input("name: ")
        calories = input("calories: ")
        protein = input("protein: ")
        fat = input("fat: ")
        carbs = input("carbs: ")
        fiber = input("fiber: ")
        ingredient_type = input("ingredient_type: ")
        add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type)


class TerminateProgram(Strategy):
    def execute(self):
        sys.exit()
