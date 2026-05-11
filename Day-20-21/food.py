from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("chocolate4")
        self.speed("fastest")

    def new_location(self):
        xcor = random.randint(-380, 380)
        ycor = random.randint(-380, 380)
        self.goto(xcor, ycor)

