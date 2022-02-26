from resource_data import MENU, resources


def report():
    print(f"Water: {resources['water']}.")
    print(f"Milk: {resources['milk']}.")
    print(f"Coffee: {resources['coffee']}.")
    print(f"Money: ${profit}")


def is_sufficient(order_ingredients):
    # TODO: 4. Check resources sufficient?
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_money():
    """Returns the total money that user input."""
    cost = float(input("Please insert money. Valid money are $1, $5, $20, and $100.: "))
    return cost


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


profit = 0
is_on = True

while is_on:
    # TODO 1: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/): ”
    user_choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()

    # TODO 2: 2. Turn off the Coffee Machine by entering “off” to the prompt
    if user_choice == "off".lower():
        is_on = False
    elif user_choice == "report".lower():
        # TODO 3: 3. Print report.
        report()
    else:
        drink = MENU[user_choice]
        # TODO: 6. Check transaction successful?
        if is_sufficient(drink["ingredients"]):
            payment = process_money()
            # TODO: 5.Process coins.
            if payment > drink["cost"]:
                change = round(payment - drink["cost"], 2)
                print(f"Here is ${change} in change.")

                profit += drink["cost"]
                # TODO: 7. Make Coffee.
                make_coffee(user_choice, drink["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")
