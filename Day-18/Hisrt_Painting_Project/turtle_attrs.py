import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

class Kasav:

    def __init__(self):
        self.turtle = Turtle()
        self.screen = Screen()

    def kasav_properties(self, sp, wd):
        self.turtle.shape("arrow")
        self.turtle.color("DarkOliveGreen4")
        self.turtle.speed(sp)
        self.turtle.width(wd)
        self.turtle.hideturtle()

    def kasav_screen_setup(self):
        self.screen.setup(width=1400, height=1000)
        self.screen.bgcolor("snow")

    def kasav_screen_exit(self):
        self.screen.exitonclick()