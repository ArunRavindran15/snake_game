from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score} ", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
