from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("snow")
screen.title("Nokia's Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")

screen.exitonclick()