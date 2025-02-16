from turtle import Turtle
from random import randint
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = Car(self.cars_speed)
        self.cars.append(car)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self, car_speed=STARTING_MOVE_DISTANCE):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[randint(0, len(COLORS)-1)])
        self.penup()
        self.setheading(180)
        self.goto(300, randint(-250, 270))
        self.car_speed = car_speed

    def move(self):
        self.goto(self.xcor() - self.car_speed, self.ycor())
