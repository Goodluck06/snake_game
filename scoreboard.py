from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier NEW", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.color('white')
        self.write(f"Score: {self.score}", align = ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def margin(self):
        self.penup()
        self.goto(280, 280)
        self.pencolor("red")
        self.pendown()
        self.goto(280, -280)
        self.goto(-280, -280)
        self.goto(-280, 280)
        self.goto(-280, 280)
        self.goto(280, 280)
        self.hideturtle()