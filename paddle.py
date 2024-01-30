from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(coordinates)

    def move_left(self):
        new_x = self.xcor() - 20
        if self.xcor() > -350:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        if self.xcor() < 350:
            self.goto(new_x, self.ycor())