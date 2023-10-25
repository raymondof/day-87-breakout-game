import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard


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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

balls = 3
game_is_on = True
unique_brick = []
balls_2_last_x = []
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move_ball()

    balls_2_last_x.append(ball.xcor())
    if len(balls_2_last_x) > 2:
        balls_2_last_x.pop(0)




    # Detect wall collision
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    # Detect floor "collision"
    if ball.ycor() < -290:
        balls -= 1
        ball.hideturtle()
        ball.clear()
        if balls > 0:
            ball = Ball()
        else:
            scoreboard.end_game()

    # Detect roof collision
    if ball.ycor() > 290:
        # ball.bounce_y()
        scoreboard.finish()

    # Detect paddle collision
    if ball.ycor() < -230 and ball.distance(paddle) < 50:
        if balls_2_last_x[0] < balls_2_last_x[1]:
            direction = 0  # ball is coming from left to right
        else:
            direction = 1  # ball is coming from right to left
        paddle_ball_x = ball.xcor() - paddle.xcor()
        print(paddle_ball_x)
        ball.paddle_bounce_y(position=paddle_ball_x, direction=direction)

    # Detect brick collision
    for brick in wall.brick_pos:
        x, y = brick
        if brick not in unique_brick:
            # calculate absolute vertical and horizontal distance from ball to brick
            x_abs_to_ball = abs(ball.xcor() - x)
            y_abs_to_ball = abs(ball.ycor() - y)
            # if both of the aforementioned distances are smaller than the size
            # of the brick (100 x 20), the ball has hit the brick
            if x_abs_to_ball < 50 and y_abs_to_ball < 10:
                # add the brick to list of unique bricks and remove it so that it can't be hit again
                unique_brick.append(brick)
                wall.remove_brick(brick)
                scoreboard.score += 1
                scoreboard.write_score()
                #scoreboard.reset()

                # Trajectory decision
                # Determine if the ball is approaching from sides or below/above
                # Bricks size 100 x 20 and to the middle half of that
                # x_0 and y_0 "cancel" the lengths of the sides
                x_0 = abs(x_abs_to_ball - 50)
                y_0 = abs(y_abs_to_ball - 10)
                # in case x_0 is greater than y_0 the ball approaches the brick from below/above
                if x_0 > y_0:
                    ball.bounce_y()
                    print("below/above hit")
                # in case y_0 is greater than y_0 the ball approaches the brick from below/above
                elif y_0 > x_0:
                    ball.bounce_x()
                    print("side hit")
                # otherwise the ball is approaching the corner
                else:
                    ball.bounce_x()
                    ball.bounce_y()
                    print("corner hit")




screen.exitonclick()
