from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput("Make a bet", "Which turtle will win the race? Enter a color: ")

is_race_on = False
turtles = []

def create_turtles_at_positions():
    y_positions = [-80, -50, -20, 10, 40, 70]
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(-230, y_positions[turtle_index])
        turtles.append(new_turtle)

create_turtles_at_positions()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've loose! The {winning_color} turtle is the winner!")
            is_race_on = False


screen.exitonclick()