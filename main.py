from data import resources

want_coffee = True


def coffee_machine():
    global want_coffee
    choice: str = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso":
        espresso()
    elif choice == "latte":
        latte()
    elif choice == "cappuccino":
        cappuccino()
    elif choice == "report":
        report()
    elif choice == "off":
        want_coffee = False


def payment():
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)
    return total


def espresso():
    if resources["water"] < 50:
        print("Sorry, there is not enough water")
        coffee_machine()
    if resources["coffee"] < 18:
        print("Sorry, there is not enough milk")
        coffee_machine()
    money_in = payment()
    if money_in < 1.5:
        print("Sorry, that is not enough money. Money refunded.")
        coffee_machine()
    else:
        change = round(money_in - 1.5, 2)
        print(f"Here is your ${change} in change.")
        print("Here is your espresso")
        resources["water"] -= 50
        resources["coffee"] -= 18
        resources["Money"] += 1.50


def latte():
    if resources["water"] < 200:
        print("Sorry, there is not enough water")
        coffee_machine()
    if resources["coffee"] < 24:
        print("Sorry, there is not enough milk")
        coffee_machine()
    if resources["milk"] < 150:
        print("Sorry, there is not enough milk")
        coffee_machine()
    money_in = payment()
    if money_in < 2.5:
        print("Sorry, that is not enough money. Money refunded.")
        coffee_machine()
    else:
        change = round(money_in - 2.5, 2)
        print(f"Here is your ${change} in change.")
        print("Here is your latte")
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150
        resources["Money"] += 2.50


def cappuccino():
    if resources["water"] < 250:
        print("Sorry, there is not enough water")
        coffee_machine()
    if resources["coffee"] < 24:
        print("Sorry, there is not enough milk")
        coffee_machine()
    if resources["milk"] < 100:
        print("Sorry, there is not enough milk")
        coffee_machine()
    money_in = payment()
    if money_in < 3.0:
        print("Sorry, that is not enough money. Money refunded.")
        coffee_machine()
    else:
        change = round(money_in - 3.0, 2)
        print(f"Here is your ${change} in change.")
        print("Here is your cappuccino")
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100
        resources["Money"] += 3.00


def report():
    for key in resources:
        print(key)
        print(resources[key])


while want_coffee:
    coffee_machine()
