def turning_off():
    """
    Turning off the machine when maintainers
    enter the secret code "off"
    """
    print("Closing all running application...")
    print("Powering off")

def print_report(resource_available, total_money):
    """
    Displaying the resource available and total income
    when the maintainers enter the secret code "report"
    """


def is_resource_suffient(resource_available, resource_requested):
    """
    Checking whether the resource left is enough
    to serve new request

    Input: 
      resource_available (dictionary)
      resource_requested (dictionary)
    Output: True of False
    """
    for ingredient in resource_available:
        if ingredient not in resource_requested:
            continue
        elif resource_available[ingredient] < resource_requested[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def is_enough_money(money_inserted, menu_cost):
    """
    Compare the user's money with actual menu cost
    """
    if money_inserted < menu_cost:
        print("Sorry that's not enough money. Money refunded")
        return False

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
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while choice not in VALID_MENU and choice not in OPERATIONAL_MENU:
        print("Invalid input")
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        turning_off
        return
    else:
        if choice == "report":
            print_report(resources, total_income)
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        else:
            enough_resources = is_resource_suffient(resources, MENU[choice]["ingredients"])
            enough_money = True
            while enough_resources:
                # if user is the maintainer and want the report
                
                    # ask to insert the coins
                    print("Please insert coins.")
                    quarters_qty = int(input("how many quarters?: "))
                    dimes_qty = int(input("how many dimes?: "))
                    nickles_qty = int(input("how many nickels?: "))
                    pennies = int(input("how many pennies?: "))
                    enough_money = is_enough_money()

        

main()
