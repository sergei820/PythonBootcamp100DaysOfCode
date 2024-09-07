from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_coffee_machine():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    drink = MenuItem('none', 0, 0, 0, 0)

    user_choice = input(f"What would you like? ({menu.get_items()}):")

    if user_choice == "off":
        return
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
        run_coffee_machine()
    elif user_choice in menu.get_items():
        drink = menu.find_drink(user_choice)
    else:
        print("There is no item with that name.")
        run_coffee_machine()

    if not coffee_maker.is_resource_sufficient(drink) or not money_machine.make_payment(drink.cost):
        run_coffee_machine()

    coffee_maker.make_coffee(drink)
    run_coffee_machine()


if __name__ == "__main__":
    run_coffee_machine()
