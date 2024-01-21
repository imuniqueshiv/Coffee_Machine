# Define a menu containing information about different drinks and their ingredients and costs.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initialize profit and resources available for making drinks.
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Define a function to check if there are enough resources to make a particular drink.
def is_resource_sufficient(order_ingredients):
    """Returns True when the order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# Define a function to process the coins inserted by the user and return the total.
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# Define a function to check if the transaction is successful based on the received money and the cost of the drink.
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if the money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

# Define a function to make a coffee by deducting the required ingredients from the resources.
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# Set a flag to control the main loop.
is_on = True

# Start the main loop for taking user orders.
while is_on:
    # Prompt the user for their choice (order, report, or turn off the machine).
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    # Check if the user wants to turn off the machine.
    if choice == "off":
        is_on = False
    # Check if the user wants to see a report of available resources and profit.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    # Process the user's drink order.
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
