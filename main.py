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

game_is_on = False
is_paused = False


def start_or_pause_game():
    global game_is_on, is_paused
    if not game_is_on:
        game_is_on = True
        game_loop()
    else:
        is_paused = not is_paused

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.onkey(fun=start_or_pause_game, key="space")
scoreboard.write_instructions()

balls = 3
unique_brick = []
balls_2_last_x = []


def game_loop():
    global balls, ball
    #TODO: integrate pause functionality
    while game_is_on:
        # if scoreboard.space_pos == 0:
        #     game_is_on = True
        # elif scoreboard.space_pos == 1:
        #     game_is_on = False
        scoreboard.write_score(balls)
        screen.update()

        ball.move_ball()

        balls_2_last_x.append(ball.xcor())
        if len(balls_2_last_x) > 2:
            balls_2_last_x.pop(0)  # keep only 2 previous coordinates for determining trajectory

        # Detect wall collision
        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.bounce_x()

        # Detect floor "collision"
        if ball.ycor() < -290:
            balls -= 1
            ball.hideturtle()
            ball.clear()
            scoreboard.write_score(balls)
            if balls > 0:
                ball = Ball()
            else:
                scoreboard.end_game()
                break

        # Detect roof collision
        if ball.ycor() > 290:
            # ball.bounce_y()
            scoreboard.finish()
            break

        # Detect paddle collision
        if ball.ycor() < -230 and ball.distance(paddle) < 50:
            # Determine the ball trajectory
            if balls_2_last_x[0] < balls_2_last_x[1]:
                direction = 0  # ball is coming from left to right
            else:
                direction = 1  # ball is coming from right to left
            # calculate balls relative position to the paddle
            # negative value means on the left and positive on the right
            paddle_ball_x = ball.xcor() - paddle.xcor()
            ball.paddle_bounce_y(position=paddle_ball_x, direction=direction)

        # Detect brick collision
        for brick in wall.brick_pos:
            x, y = brick  # bricks coordinates
            if brick not in unique_brick:  # check if brick has already been hit, thus removed
                # calculate absolute vertical and horizontal distance from ball to brick
                x_abs_to_ball = abs(ball.xcor() - x)
                y_abs_to_ball = abs(ball.ycor() - y)
                # if both of the aforementioned distances are smaller than the size
                # of the brick (100 x 20), measured from the middle, the ball has hit the brick
                if x_abs_to_ball < 50 and y_abs_to_ball < 10:
                    unique_brick.append(brick)  # # add the brick to list of unique bricks
                    wall.remove_brick(brick)  # and remove it so that it can't be hit again
                    scoreboard.score += 1  # add score
                    scoreboard.write_score(balls)  # write it on the screen

                    # Trajectory decision
                    # Determine if the ball is approaching from sides or below/above
                    # Bricks size 100 x 20 and to the middle half of that
                    # x_0 and y_0 "cancel" the lengths of the sides
                    x_0 = abs(x_abs_to_ball - 50)
                    y_0 = abs(y_abs_to_ball - 10)
                    # in case x_0 is greater than y_0 the ball approaches the brick from below/above
                    if x_0 > y_0:
                        ball.bounce_y()
                    # in case y_0 is greater than y_0 the ball approaches the brick from below/above
                    elif y_0 > x_0:
                        ball.bounce_x()
                    # otherwise the ball is approaching the corner
                    else:
                        ball.bounce_x()
                        ball.bounce_y()
        time.sleep(0.01)


screen.exitonclick()
