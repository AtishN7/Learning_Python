from turtle_attrs import Kasav

class HirstDrawing(Kasav):

    def __init__(self):
        super().__init__()

    def draw(self, rgb_value):
        self.turtle.color(rgb_value)
        self.turtle.dot(20)

    def pen_up(self):
        self.turtle.penup()

    def pen_down(self):
        self.turtle.pendown()

    def dot_forward(self, paces):
        self.turtle.forward(paces)

    def set_direction(self, angle):
        self.turtle.setheading(angle)

    def set_position(self, x, y):
        self.turtle.teleport(x,y)

