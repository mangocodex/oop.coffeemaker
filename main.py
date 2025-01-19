from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_item = Menu()

is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if order == "off":
        print("Powering down.")
        is_on = False
    elif order == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif order:
        my_coffee_maker.is_resource_sufficient(drink=order)