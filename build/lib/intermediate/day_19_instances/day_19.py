from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.bk(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def reset():
    # tim.clear()
    # tim.penup()
    tim.home()
    tim.clear()
    # tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()
