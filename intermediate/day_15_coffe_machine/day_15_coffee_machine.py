import menu


def run_coffee_machine():

    coffee_machine = CoffeeMachine(money=2)

    customer_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if customer_choice in ["espresso", "latte", "cappuccino"]:
        pass
    elif customer_choice == "off":
        return
    elif customer_choice == "report":
        coffee_machine.print_report()
        run_coffee_machine()
    else:
        print("Please, choose a beverage from the list")
        run_coffee_machine()


class CoffeeMachine:
    water: int
    milk: int
    coffee: int
    money: float

    def __init__(self, money: float):
        self.water = menu.resources["water"]
        self.milk = menu.resources["milk"]
        self.coffee = menu.resources["coffee"]
        self.money = money

    def print_report(self):
        print(self.__str__())

    def check_resources(self, drink: str):
        water_required = menu.MENU[drink]["ingredients"]["water"]
        milk_required = menu.MENU[drink]["ingredients"]["milk"]
        coffee_required = menu.MENU[drink]["ingredients"]["coffee"]
        if self.water < water_required:
            print("Sorry there is not enough water.")
        elif self.milk < milk_required:
            print("Sorry there is not enough milk.")
        elif self.coffee < coffee_required:
            print("Sorry there is not enough coffee.")

    def __str__(self):
        return f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}"


if __name__ == "__main__":
    run_coffee_machine()


