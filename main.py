from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#tworz obiekt z Class
#bewerages = Menu()
#print(bewerages.get_items())  #latte/espresso/cappuccino/

#tworzy nowy obiekt - Class MenuItem
#order = bewerages.find_drink("latte")
# print(order)  #<menu.MenuItem object at 0x0000001A77C90E00>
# print(order.name)  #latte
# print(order.cost)  #2.5
# print(order.ingredients)  #{'water': 200, 'milk': 150, 'coffee': 24}

# tworz obiekt z Class
# coffee_maker = CoffeeMaker()
# # #wyswietl raport resources
# coffee_maker.report()
# #returns True or False - czy jest wystarczajaco skladnikow
# print(coffee_maker.is_resource_sufficient(order))
# #odejmuje skladniki ze stanu i wyswietla enjoy your coffee
# coffee_maker.make_coffee(order)
#
# # tworz obiekt z Class
# money_machine = MoneyMachine()
# #stan kasy
# print(money_machine.report())
#
# print(money_machine.make_payment(order.cost))

#######################Przerabiam kod z Day15
bewerages = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_turn_off = False
while machine_turn_off == False:
    users_choice = input(f"What would you like? {(bewerages.get_items())}:")

    if users_choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif users_choice == "off":
        machine_turn_off = True
        print("Machine is off")

    else:
        order = bewerages.find_drink(users_choice)
        if coffee_maker.is_resource_sufficient(order) == True:
            if money_machine.make_payment(order.cost) == True:
                coffee_maker.make_coffee(order)

