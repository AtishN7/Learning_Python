# from turtle import Turtle, Screen
#
# kasav = Turtle()
# print(kasav)
# kasav.shape("turtle")
# kasav.color("DarkOliveGreen")
# kasav.forward(100)
# kasav.left(90)
# kasav.forward(100)
# kasav.right(90)
# kasav.forward(100)
#
# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.header_style = "upper"
table.align = "l"
print(table)