from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.move_x = 0.3
        self.move_y = 0.3
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.move_x *= -1

    def bounce_y(self):
        self.move_y *= -1