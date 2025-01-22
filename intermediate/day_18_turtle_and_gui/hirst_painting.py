import turtle
import random
import colorgram

# requirements:
# 10x10
# dot size=20; distance_between=50

def start_app():
    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.hideturtle()
    timmy.speed(10)
    turtle.colormode(255)
    timmy.pu()

    colors = colorgram.extract("image.jpg", 15)

    def get_picture_color():
        return colors[random.randint(0,7)].rgb

    def draw_dots(dots_num):
        for _ in range(dots_num):
            timmy.dot(20, get_picture_color())
            timmy.fd(50)

    def turn_back_left():
        timmy.left(90)
        timmy.fd(50)
        timmy.left(90)
        timmy.fd(50)

    def turn_back_right():
        timmy.right(90)
        timmy.fd(50)
        timmy.right(90)
        timmy.fd(50)

    def draw_two_lines(repeat):
        for _ in range(repeat):
            draw_dots(10)
            turn_back_left()
            draw_dots(10)
            turn_back_right()

    timmy.setheading(215)
    timmy.fd(250)
    timmy.setheading(0)
    draw_two_lines(5)

    screen = turtle.Screen()
    screen.exitonclick()

if __name__ == "__main__":
    start_app()