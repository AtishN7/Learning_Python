from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.scales = []
        self.create_snake_body()
        self.head = self.scales[0]

    def create_snake_body(self):
        for t in COORDINATES:
            scale = Turtle("square")
            scale.color("DarkGoldenrod3")
            scale.penup()
            scale.goto(t)
            self.scales.append(scale)

    def move(self):
        for num in range(len(self.scales) - 1, 0, -1):
            new_x = self.scales[num - 1].xcor()
            new_y = self.scales[num - 1].ycor()
            self.scales[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

