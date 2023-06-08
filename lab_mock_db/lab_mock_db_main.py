import csv
import ingredients_functions

filename = 'ingredients.csv'

our_dialect = csv.excel
our_dialect.delimiter = ';'
our_dialect.quoting = csv.QUOTE_NONNUMERIC

with open(filename, 'r', encoding='UTF-8', newline='') as ingredients_file:
    # reader = csv.DictReader(ingredients_file, dialect=our_dialect)
    reader = csv.reader(ingredients_file, dialect=our_dialect)
    ingredients_file.readline()  # Ignore Headers
    for row in reader:
        ingredients_functions.add_ingredient(*row)

strategy_map = {
    "1": ingredients_functions.AddNewIngredient(),
    "2": ingredients_functions.ListIngredients(),
    "3": ingredients_functions.ListIngredientsByName(),
    "0": ingredients_functions.TerminateProgram()
}

while True:
    print("", "1 – Dodanie nowego składnika", "2 – Wyświetlenie wszystkich składników",
          "3 – Wyświetlenie składnika po nazwie", "0 – Zakończenie programu", "Wybierz co chcesz zrobić: ", sep="\n")
    decision = input("> ")

    if decision not in strategy_map:
        print("Proszę wybrać poprawną wartość!")
    else:
        strategy_map[decision].execute()
