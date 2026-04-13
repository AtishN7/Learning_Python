from turtle_attributes import Kasav
import random

class MoveTurtle(Kasav):

    def __init__(self):
        super().__init__()

    def move_paces(self, paces):
        self.turtle.forward(paces)

    def square_move(self, paces, angle):
        for i in range(4):
            self.turtle.right(angle)
            self.turtle.forward(paces)

    def dotted_line(self, line_paces):
        for l in range(10):
            # self.turtle.forward(line_paces)
            # self.turtle.teleport(x=self.turtle.xcor()+line_paces)
            # self.turtle.forward(line_paces)

            self.turtle.forward(line_paces)
            self.turtle.pendown()
            self.turtle.forward(line_paces)
            self.turtle.penup()

    def draw_pattern(self, shape_sides, shape_length):
        rainbow = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
        i = 3
        while i < shape_sides:
            self.turtle.color(random.choice(rainbow))
            for _ in range(i):
                self.turtle.forward(shape_length)
                angle = 360/i
                self.turtle.right(angle)
            i += 1
