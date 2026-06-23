from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
COFFEE_MAKER = CoffeeMaker()
MONEY_MACHINE = MoneyMachine()

def main():
    total_income = 0

    while True:
        # ask the user choice
        choice = input(f"What would you like? ({MENU.get_items()}): ")

        if choice == "off":
            # turning off the machine
            break
        elif choice == "report":
            # printing the report
            COFFEE_MAKER.report()
            MONEY_MACHINE.report()
            continue
        else:
            # ask the user again if the choice is invalid
            drink = MENU.find_drink(choice)
            while drink is None:
                choice = input(f"What would you like? ({MENU.get_items()}): ")
                drink = MENU.find_drink(choice)

            resource_sufficient = COFFEE_MAKER.is_resource_sufficient(drink)
            if resource_sufficient:
                payment_success = MONEY_MACHINE.make_payment(drink.cost)
                if payment_success:
                    COFFEE_MAKER.make_coffee(drink)

    print("Closing the application...")
    print("Powering off")

main()
