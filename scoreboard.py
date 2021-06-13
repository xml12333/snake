from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.refresh()

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGMENT, font=FONT)

    def geme_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGMENT, font=FONT)
