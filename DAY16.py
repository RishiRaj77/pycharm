

# from turtle import Turtle ,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
#
# timmy.forward(150)
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = [" BIKE ", "ability"]
table.add_row([" SHO ", " FLAME "])
table.add_row([" KIOCHI ", " THUNDER "])
table.add_row([" GABU ", " IMPACT "])

print(table.align)
print(table)

