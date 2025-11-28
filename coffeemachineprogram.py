from data import Menu
from data import Resources

profit = 0

def has_resources(drink):
    ingredients = drink["ingrediants"]

    for item in ingredients:
        if Resources[item] < ingredients[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def make_drink(drink):
    global profit

    ingredients = drink["ingrediants"]

    for item in ingredients:
        Resources[item] -= ingredients[item]

    profit += drink["cost"]

    print(f"Your {drink_name} is ready! Enjoy!")


while True:
    choice = input("What would you like? (Tea/Coffee/BlackTea): ").strip()

    if choice.lower() == "off":
        break

    elif choice.lower() == "report":
        print(f"Water: {Resources['Water']}ml")
        print(f"Sugar: {Resources['Sugar']}g")
        print(f"TeaPowder: {Resources['TeaPowder']}g")
        print(f"CoffeePowder: {Resources['CoffeePowder']}g")
        print(f"BlackTeaPowder: {Resources['BlackTeaPowder']}g")
        print(f"Money: {profit} Rs.\n")
    
    elif choice in Menu:
        drink_name = choice
        drink = Menu[choice]

        if has_resources(drink):
            make_drink(drink)

    else:
        print("Invalid input. Try again.")
