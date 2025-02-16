import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def start_app():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Crossroads")
    screen.tracer(0)

    player = Player()

    screen.listen()
    screen.onkey(player.go_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        #implement cars

    screen.exitonclick()


if __name__ == "__main__":
    start_app()
