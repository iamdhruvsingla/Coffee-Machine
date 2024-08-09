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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

change_given_by_customer = 0

def order():
    global choice
    choice = input("​What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
        print(f"Money: {profit}")
        order()

def is_resource_sufficient():
    order()
    if choice == "off":
        return
    for resource in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}")
            is_resource_sufficient()
    else:
        process_coins()

profit = 0

def process_coins():
    global profit
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    change_given_by_customer = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    if MENU[choice]["cost"] > change_given_by_customer:
        print("Sorry this is not enough Money, it is refunded.")
        is_resource_sufficient()
    else:
        change_given_by_machine = round(change_given_by_customer - MENU[choice]["cost"], 2)
        print(f"Here is {change_given_by_machine} in change.")
        print(f"Here is your {choice}, Enjoy!")
        profit += MENU[choice]["cost"]
        for resource in MENU[choice]["ingredients"]:
            resources[resource] -= MENU[choice]["ingredients"][resource]
        change_given_by_customer = 0
        is_resource_sufficient()

is_resource_sufficient()