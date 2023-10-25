from turtle import Turtle
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.write_score()

    def write_score(self):
        self.clear()

        self.write(f"Score: {self.score} "
                   f"High score: {self.high_score}",
                   move=False, align="center", font=FONT)
        #self.reset()

    def finish(self):
        self.clear()

        self.write(f"You have finished the game by breaking {self.score} bricks",
                   move=False, align="center", font=FONT)

    def end_game(self):
        self.clear()

        self.write(f"Game over! Better luck next time!",
                   move=False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.write_score()

    def update_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
