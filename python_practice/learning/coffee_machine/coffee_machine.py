
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

coin_types = {
    "penny": .01,
    "nickel": .05,
    "dime": .10,
    "quarter": .25,
}


def machine_report(resources_left):
    for key in resources_left:
        if key in ('milk', 'water'):
            print(f"{key}: {resources_left[key]}ml")
        elif key == 'coffee':
            print(f"{key}: {resources_left[key]}g")
        elif 'money' in key:
            print(f"{key}: ${resources_left[key]}")
        else:
            print("money: $0.00")


def check_resources(selection):
    resources_left = resources
    request = MENU[selection]['ingredients']
    for key in request:
        if key in request and key in resources_left:
            amt_left = resources_left[key] - request[key]
            if amt_left < 0:
                print(f"Sorry there is not enough of {key}.")
                return False
    return True


def int_validation(number):
    while True:
        try:
            value = int(input(number))
            return value
        except ValueError:
            print("Invalid entry, must be an integer.")


def process_coins():
    quarters = int_validation("How many quarters? ")
    dimes = int_validation("How many dimes? ")
    nickels = int_validation("How many nickels? ")
    pennies = int_validation("How many pennies? ")
    total_coins = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
    return total_coins


def transaction(coffee, coins_in):
    request = MENU[coffee]['ingredients']
    cost = MENU[coffee]['cost']
    if cost > coins_in:
        print(
            f"    Sorry that's not enough money.\n    You gave in ${coins_in:.2f} and the {coffee} costs ${cost:.2f}. Money Refunded.")
    elif cost <= coins_in:
        for key in request:
            resources[key] = resources[key] - request[key]
        if 'money' in resources:
            resources['money'] += cost
        else:
            resources['money'] = cost
        if cost < coins_in:
            change = round(coins_in - cost, 2)
            print(f"Here is ${change:.2f} dollars in change.")
        print(f"Here is your {coffee}. Enjoy!")


menu_list = []
for key in MENU:
    menu_list.append(key)


def coffee_maker():
    turn_off = False
    while not turn_off:
        coffee_request = input(
            "What would you like? (espresso/latte/cappuccino): ")
        if coffee_request == 'report':
            machine_report(resources)
        elif coffee_request == 'end':
            turn_off = True
        elif coffee_request in menu_list:
            enough_resources = check_resources(coffee_request)
            if enough_resources:
                print("Please insert coins.")
                coins_inserted = process_coins()
                transaction(coffee_request, coins_inserted)


coffee_maker()
