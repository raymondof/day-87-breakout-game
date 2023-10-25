from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.move_x = 3
        self.move_y = 3
        self.move_speed = 3

    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.move_x *= -1

    def bounce_y(self):
        self.move_y *= -1
        print(f"bounce_e {self.move_y}")

    def paddle_bounce_y(self, position, direction):
        angle = position / 50
        print(f"paddle position {position}")
        if position < 10 and position > -10:
            self.move_y *= -1
            print("mailan keskelle")
        elif position < -10 and direction == 0:
            print("mailan vasen reuna")
            self.move_y *= -1# + self.move_speed * angle
            self.move_x *= -1# - self.move_speed * angle
        elif position > 10 and direction == 1:
            print("mailan oikea reuna")
            self.move_y *= -1
            self.move_x *= -1# self.move_speed * angle
        else:
            self.move_y *= -1
        # self.move_y += position
        # self.move_x -= position
        print(f"paddle_bounce_y {self.move_y}")
        print(f"paddle_bounce_x {self.move_x}")


