from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall


screen = Screen()
screen.setup(width=800, height=600, startx=550, starty=250)
screen.bgcolor("black")
screen.title("Breakout")
# turns turtle animation off, making things appear immediately on the screen
screen.tracer(0)

paddle_start_coordinates = (0, -250)
paddle = Paddle(paddle_start_coordinates)

ball = Ball()
wall = Wall()
wall.build_wall()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
print(f"wall.brick_pos {wall.brick_pos}")
print(f"wall.brick_pos {wall.brick_pos[1:]}")
#print(wall.brick_pos[1:])

counter = 0
game_is_on = True
unique_brick = []
while game_is_on:
    screen.update()
    ball.move_ball()

    # Detect wall collision
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.bounce_x()

    # Detect roof collision
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # Detect paddle collision
    if ball.ycor() < -250 and ball.distance(paddle) < 50:
        ball.bounce_y()


    for brick in wall.brick_pos:
        x, y = brick
        if brick not in unique_brick:
            if abs(ball.ycor() - y) < 10 and abs(ball.xcor() - x) < 50:
                unique_brick.append(brick)
                wall.remove_brick(brick)

screen.exitonclick()