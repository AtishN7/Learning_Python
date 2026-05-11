from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Nokia's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Check for wall collision
    if snake.head.distance(food) < 15:
        scoreboard.color("green")
        scoreboard.update_score()
        food.new_location()
        snake.extend_scale()

    #Check for wall collision
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        game_on = False
        scoreboard.color("red")
        scoreboard.game_over()

    #Check for tail end collision
    for scale in snake.scales[1:]:
        if snake.head.distance(scale) < 1:
            game_on = False
            scoreboard.color("red")
            scoreboard.game_over()

screen.exitonclick()