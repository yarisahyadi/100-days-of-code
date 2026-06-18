def user_input():
    """
    Asking the user input regarding their menu choice
    Output: a string of user's choice
    """
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def turning_off():
    """
    Turning off the machine when maintainers
    enter the secret code "off".
    """
    print("Closing all running applications...")
    print("Powering off")

def print_report(resource_available, total_money):
    """
    Displaying the resource available and total income
    when the maintainers enter the secret code "report".
    Input: 
      resource_available (dictionary)
      total_money (float)
    """
    for ingredient in resource_available:
        if ingredient == "coffee":
            print(f"{ingredient.capitalize()}: {resource_available[ingredient]}g")
        else:
            print(f"{ingredient.capitalize()}: {resource_available[ingredient]}ml")
    print(f"Money: ${total_money}")


def is_resource_sufficient(resource_available, resource_requested):
    """
    Checking whether the resource left is enough
    to serve new request.
    Input: 
      resource_available (dictionary)
      resource_requested (dictionary)
    Output: True of False
    """
    for ingredient in resource_requested:
        if resource_available[ingredient] < resource_requested[ingredient]:
            return False
    return True
    
def calculate_money():
    """
    Function to calculate total of the money inserted by the user.
    Output: float
    """
    quarters_qty = int(input("how many quarters?: "))
    dimes_qty = int(input("how many dimes?: "))
    nickels_qty = int(input("how many nickels?: "))
    pennies_qty = int(input("how many pennies?: "))
    return quarters_qty * 0.25 + dimes_qty * 0.1 + nickels_qty * 0.05 + pennies_qty * 0.01

def main():
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

    OPERATIONAL_MENU = ["off", "report"]
    VALID_MENU = list(MENU.keys())
    total_income = 0

    # ask user the input
    choice = user_input()
    while choice not in VALID_MENU and choice not in OPERATIONAL_MENU:
        print("Invalid input")
        choice = user_input()
    
    while choice != "off":
        if choice == "report":
            print_report(resources, total_income)
        else:
            drink = MENU[choice]
            enough_resources = is_resource_sufficient(resources, drink["ingredients"])
            if enough_resources:
                # ask to insert the coins
                print("Please insert coins.")
                money = calculate_money()
                if money >= drink["cost"]:
                    if money > drink["cost"]:
                        change = round(money - drink["cost"], 2)
                        print(f"Here is ${change} dollars in change.")
                    total_income += drink["cost"]
                    for ingredient in drink["ingredients"]:
                        resources[ingredient] -= drink["ingredients"][ingredient]
                    print(f"Here is your {choice}. Enjoy!")
                else:
                    print(f"Sorry there is not enough {ingredient}")

        choice = user_input()
                
    turning_off()
    return

main()
