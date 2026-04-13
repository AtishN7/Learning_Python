from turtle import Turtle, Screen

class Kasav:

    def __init__(self):
        self.turtle = Turtle()
        self.screen = Screen()

    def kasav_shape(self, sp):
        self.turtle.shape("turtle")
        self.turtle.color("DarkOliveGreen4")
        self.turtle.speed(sp)

    def kasav_screen_setup(self):
        self.screen.setup(width=1200, height=800)
        self.screen.bgcolor("snow")

    def kasav_screen_exit(self):
        self.screen.setup(width=1200, height=800)
        self.screen.exitonclick()