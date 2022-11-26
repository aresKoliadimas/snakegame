from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.write_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.clear()
        self.write_score()

    def write_score(self):
        with open("data.txt") as data:
            self.write(f"Score: {self.score} | High Score: {data.read()}", align=ALIGNMENT, font=FONT)