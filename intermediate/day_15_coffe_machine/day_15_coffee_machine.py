import menu


def run_coffee_machine():

    coffee_machine = CoffeeMachine()

    customer_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if customer_choice in ["espresso", "latte", "cappuccino"]:
        coffee_machine.check_resources(customer_choice)
        coffee_machine.process_coins()
        coffee_machine.is_enough_money(customer_choice)
        coffee_machine.make_coffee(customer_choice)
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

    def __init__(self):
        self.water = menu.resources["water"]
        self.milk = menu.resources["milk"]
        self.coffee = menu.resources["coffee"]
        self.money = 0

    def print_report(self):
        print(self.__str__())

    def check_resources(self, drink: str):
        if drink in ["latte", "cappuccino"]:
            milk_required = menu.MENU[drink]["ingredients"]["milk"]
            if self.milk < milk_required:
                print("Sorry there is not enough milk.")
                run_coffee_machine()

        water_required = menu.MENU[drink]["ingredients"]["water"]
        coffee_required = menu.MENU[drink]["ingredients"]["coffee"]

        if self.water < water_required:
            print("Sorry there is not enough water.")
            run_coffee_machine()
        elif self.coffee < coffee_required:
            print("Sorry there is not enough coffee.")
            run_coffee_machine()

    def process_coins(self):
        print("Please, insert coins")
        quarters = int(input("quarters ($0.25): "))
        dimes = int(input("dimes ($0.10): "))
        nickles = int(input("nickles ($0.05): "))
        pennies = int(input("pennies ($0.01): "))
        self.money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        print(f"Money in Coffee Machine: ${str(self.money)}")
        # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

    def is_enough_money(self, drink):
        if self.money < menu.MENU[drink]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            self.money = 0
            run_coffee_machine()
            return False
        elif self.money > menu.MENU[drink]["cost"]:
            change = round(self.money - menu.MENU[drink]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
            self.money = 0

    def make_coffee(self, drink):
        self.print_report()
        self.water -= menu.MENU[drink]["ingredients"]["water"]
        self.coffee -= menu.MENU[drink]["ingredients"]["coffee"]
        self.milk -= menu.MENU[drink]["ingredients"]["milk"]
        self.print_report()

    def __str__(self):
        return (f"Water: {self.water}ml\n"
                f"Milk: {self.milk}ml\n"
                f"Coffee: {self.coffee}g\n"
                f"Money: ${self.money}")


if __name__ == "__main__":
    run_coffee_machine()


