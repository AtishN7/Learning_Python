from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Georgia", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,360)
        self.color("white")
        self.score = 0
        self.write_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(arg=f"GAME OVER!! Final Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)


