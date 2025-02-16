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
    # car = Car()
    car_manager = CarManager()
    counter = 0

    game_is_on = True
    while game_is_on:
        counter += 1
        if counter % 8:
            car_manager.generate_cars()

        for car in car_manager.cars:
            car.move()

        time.sleep(0.1)
        screen.update()

        # car.move()
        for car in car_manager.cars:
            if player.distance(car) < 10:
                print("Car accident")
                game_is_on = False

        if player.ycor() >= FINISH_LINE_Y:
            player.reset_position()
            scoreboard.score += 1
            scoreboard.update_scoreboard()
            car_manager.increase_speed()

    screen.exitonclick()


if __name__ == "__main__":
    start_app()
