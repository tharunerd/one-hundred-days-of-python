# # # from some import some_variable
# # # print (some_variable)
# #
# #
# # from turtle import Turtle, Screen
# #
# # tharun = Turtle()
# # print(tharun)
# # tharun.shape("turtle")
# # tharun.color("teal")
# # tharun.forward(100)
# # tharun.right(50)
# # # tharun.backward
# #
# # my_screen = Screen()
# # print(my_screen.canvwidth)
# # print (my_screen.canvheight)
# # my_screen.exitonclick()
# #import prettytable
#
# from prettytable import PrettyTable
#
# create_table = PrettyTable()
# create_table.add_column("shape",["circle","triangle","square"])
# create_table.add_column("sides",[ "0","3","4"])
# create_table.allign = "l"
# print(create_table)
#
#
#
#
#
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)


