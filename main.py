from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600, startx=550, starty=250)
screen.bgcolor("black")
screen.title("Breakout")

paddle_start_coordinates = (0, -250)
paddle = Paddle(paddle_start_coordinates)

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

screen.exitonclick()