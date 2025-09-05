from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def start_game():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(800, 600)
    screen.title("Paddle")
    screen.tracer(0)

    right_paddle = Paddle((380, 0))
    screen.listen()
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")

    left_paddle = Paddle((-380, 0))
    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(left_paddle.go_down, "s")

    ball = Ball()

    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()

        if (ball.xcor() > 340 and ball.distance(right_paddle) < 50 or
                (ball.distance(left_paddle) < 50 and ball.xcor() < -340)):
            ball.x_bounce()
            ball.move_speed *= 0.9
        elif ball.xcor() > 370:
            ball.move_speed = 0.1
            ball.reset_position()
            scoreboard.l_point()
        elif ball.xcor() < -370:
            ball.move_speed = 0.1
            ball.reset_position()
            scoreboard.r_point()

        if scoreboard.l_score >= 5:
            game_is_on = False
        elif scoreboard.l_score >= 5:
            game_is_on = False


    screen.exitonclick()


# create a game field
# create a starting line with random ball direction
# ball appears
# angle of flight
# create two pongs
# game with a friend
# game with a bot
# ball logic (45 degrees, mirrored angle)


if __name__ == "__main__":
    start_game()
