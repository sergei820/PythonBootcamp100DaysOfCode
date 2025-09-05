import menu


def run_coffee_machine():

    coffee_machine = CoffeeMachine()

    customer_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if customer_choice in ["espresso", "latte", "cappuccino"]:
        coffee_machine.check_resources(customer_choice)
        coffee_machine.process_coins()
        coffee_machine.check_if_money_enough(customer_choice)
        coffee_machine.make_coffee(customer_choice)
        print(f"“Here is your {customer_choice}. Enjoy!”")
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
        self.print_report()
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
        """Calculates the total sum, sets the amount of money to the coffe machine"""
        print("Please, insert coins")
        self.money += int(input("quarters: ")) * 0.25
        self.money += int(input("dimes: ")) * 0.10
        self.money += int(input("nickles: ")) * 0.05
        self.money += int(input("pennies: ")) * 0.01

        print(f"Money in Coffee Machine: ${str(self.money)}")

    def check_if_money_enough(self, drink):
        drink_cost = menu.MENU[drink]["cost"]

        if self.money < drink_cost:
            print("Sorry that's not enough money. Money refunded.")
            self.money = 0
            run_coffee_machine()
        elif self.money > drink_cost:
            change = round(self.money - menu.MENU[drink]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
            self.money += drink_cost

    def make_coffee(self, drink):
        self.water -= menu.MENU[drink]["ingredients"]["water"]
        self.coffee -= menu.MENU[drink]["ingredients"]["coffee"]
        if drink != "espresso":
            self.milk -= menu.MENU[drink]["ingredients"]["milk"]
            self.print_report()

    def __str__(self):
        return (f"Water: {self.water}ml\n"
                f"Milk: {self.milk}ml\n"
                f"Coffee: {self.coffee}g\n"
                f"Money: ${round(self.money, 2)}")


if __name__ == "__main__":
    run_coffee_machine()


