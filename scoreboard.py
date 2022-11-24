from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
