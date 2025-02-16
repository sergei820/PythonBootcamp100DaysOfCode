import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import Car, CarManager
from scoreboard import Scoreboard


def start_app():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Crossroads")
    screen.tracer(0)

    player = Player()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.go_up, "Up")
    car_manager = CarManager()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)

        car_manager.generate_car()

        for car in car_manager.cars:
            car.move()

        screen.update()

        for car in car_manager.cars:
            if player.distance(car) < 20:
                scoreboard.game_over()
                game_is_on = False

        if player.ycor() >= FINISH_LINE_Y:
            player.reset_position()
            scoreboard.level += 1
            scoreboard.update_scoreboard()
            car_manager.increase_speed()

    screen.exitonclick()


if __name__ == "__main__":
    start_app()
