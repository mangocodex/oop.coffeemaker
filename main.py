from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    drink = menu.find_drink(order)
    if order == "off":
        print("Powering down.")
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.has_enough_resources(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)