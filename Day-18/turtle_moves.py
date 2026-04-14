from turtle_attributes import Kasav
import random

class MoveTurtle(Kasav):

    def __init__(self):
        super().__init__()

    def random_colour(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def move_paces(self, paces):
        self.turtle.forward(paces)

    def square_move(self, paces, angle):
        for i in range(4):
            self.turtle.color(self.random_colour())
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
        i = 3
        while i < shape_sides:
            self.turtle.color(self.random_colour())
            for _ in range(i):
                self.turtle.forward(shape_length)
                angle = 360/i
                self.turtle.right(angle)
            i += 1

    def random_walk(self, paces):
        movements = [self.turtle.right, self.turtle.left]
        # directions = [0, 90, 180, 270]
        for _ in range(50):
            self.turtle.color(self.random_colour())
            self.turtle.forward(paces)
            random.choice(movements)(90)
            # self.turtle.setheading(random.choice(directions))

    def spirograph(self, radius, degrees):
        heading = 0
        for _ in range(int(360/degrees)):
            self.turtle.color(self.random_colour())
            self.turtle.circle(radius=radius,steps=200)
            heading = heading + degrees
            self.turtle.setheading(heading)

