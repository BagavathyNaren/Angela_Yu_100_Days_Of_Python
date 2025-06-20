from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isCoffeeMachineOn = True

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
coffeeMenu = Menu()

while isCoffeeMachineOn:
    menu_options  = coffeeMenu.get_items()
    choice = input(f"“What would you like? ({menu_options}): ”").lower()
    if choice == 'off':
        isCoffeeMachineOn = False
    elif 'report' in choice:
        coffeeMaker.report()   
        moneyMachine.report()
    else:
        drink = coffeeMenu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost): # type: ignore
            coffeeMaker.make_coffee(drink)