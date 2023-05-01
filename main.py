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

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
profit = 0
on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit:.2f}")

    elif choice == 'off':
        on = False
    elif choice == 'espresso':
        if resources['water'] < MENU["espresso"]['ingredients']['water']:
            print("Sorry, there is not enough water.")
        elif resources['coffee'] < MENU["espresso"]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarter_amount = int(input("How many quarters? "))
            dime_amount = int(input("How many dimes? "))
            nickle_amount = int(input("How many nickles? "))
            pennie_amount = int(input("How many pennies? "))
            money = quarters * quarter_amount + dimes * dime_amount + nickles * nickle_amount + pennies * pennie_amount
            money = round(money, 2)
            if money < MENU['espresso']['cost']:
                print("Sorry, that's not enough money. Money refunded.")
            elif money > MENU['espresso']['cost']:
                refund = round(money - MENU['espresso']['cost'], 2)
                resources['water'] -= MENU["espresso"]['ingredients']['water']
                resources['coffee'] -= MENU["espresso"]['ingredients']['coffee']
                profit += MENU['espresso']['cost']
                print(f"Here is your refund ${refund:.2f}")
                print("Here is your espresso. Enjoy! ☕️😋")
            else:
                resources['water'] -= MENU["espresso"]['ingredients']['water']
                resources['coffee'] -= MENU["espresso"]['ingredients']['coffee']
                profit += MENU['espresso']['cost']
                print("Here is your espresso. Enjoy!☕️😋")

    elif choice == 'latte':
        if resources['water'] < MENU["latte"]['ingredients']['water']:
            print("Sorry, there is not enough water.")
        elif resources['milk'] < MENU["latte"]['ingredients']['milk']:
            print("Sorry, there is not enough milk.")
        elif resources['coffee'] < MENU["latte"]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarter_amount = int(input("How many quarters? "))
            dime_amount = int(input("How many dimes? "))
            nickle_amount = int(input("How many nickles? "))
            pennie_amount = int(input("How many pennies? "))
            money = quarters * quarter_amount + dimes * dime_amount + nickles * nickle_amount + pennies * pennie_amount
            money = round(money, 2)
            if money < MENU['latte']['cost']:
                print("Sorry, that's not enough money. Money refunded.")
            elif money > MENU['latte']['cost']:
                refund = round(money - MENU['latte']['cost'], 2)
                resources['water'] -= MENU["latte"]['ingredients']['water']
                resources['milk'] -= MENU["latte"]['ingredients']['milk']
                resources['coffee'] -= MENU["latte"]['ingredients']['coffee']
                profit += MENU['latte']['cost']
                print(f"Your refund is ${refund:.2f}")
                print("Here is your latte. Enjoy!☕️😋")
            else:
                resources['water'] -= MENU["latte"]['ingredients']['water']
                resources['milk'] -= MENU["latte"]['ingredients']['milk']
                resources['coffee'] -= MENU["latte"]['ingredients']['coffee']
                profit += MENU['latte']['cost']
                print("Here is your latte. Enjoy!☕️😋")

    elif choice == 'cappuccino':
        if resources['water'] < MENU["cappuccino"]['ingredients']['water']:
            print("Sorry, there is not enough water.")
        elif resources['milk'] < MENU["cappuccino"]['ingredients']['milk']:
            print("Sorry, there is not enough milk.")
        elif resources['coffee'] < MENU["cappuccino"]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarter_amount = int(input("How many quarters? "))
            dime_amount = int(input("how many dimes? "))
            nickle_amount = int(input("how many nickles? "))
            pennie_amount = int(input("how many pennies? "))
            money = quarters * quarter_amount + dimes * dime_amount + nickles * nickle_amount + pennies * pennie_amount
            money = round(money, 2)
            if money < MENU['cappuccino']['cost']:
                print("Sorry, that's not enough money. Money refunded.")
            elif money > MENU['cappuccino']['cost']:
                refund = round(money - MENU['cappuccino']['cost'], 2)
                resources['water'] -= MENU["cappuccino"]['ingredients']['water']
                resources['milk'] -= MENU["cappuccino"]['ingredients']['milk']
                resources['coffee'] -= MENU["cappuccino"]['ingredients']['coffee']
                profit += MENU['cappuccino']['cost']
                print(f"Your refund is ${refund:.2f}")
                print("Here is your cappuccino. Enjoy!☕️😋")
            else:
                resources['water'] -= MENU["cappuccino"]['ingredients']['water']
                resources['milk'] -= MENU["cappuccino"]['ingredients']['milk']
                resources['coffee'] -= MENU["cappuccino"]['ingredients']['coffee']
                profit += MENU['cappuccino']['cost']
                print("Here is your cappuccino. Enjoy!☕️😋")
