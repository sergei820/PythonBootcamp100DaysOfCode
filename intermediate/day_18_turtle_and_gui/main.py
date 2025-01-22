import turtle
import random


def start_app():
    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.color("red")

    timmy.speed(10)

    turtle.colormode(255)

    # def draw_dashed(turtle: Turtle, line_length: int):
    #     for _ in range(line_length):
    #         turtle.pencolor("white")
    #         turtle.forward(10)
    #         turtle.pencolor("blue")
    #         turtle.forward(10)
    #
    # for _ in range(4):
    #     draw_dashed(timmy, 10)
    #     timmy.right(90)

    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    # 1.
    # def draw_shape(sides_num):
    #     for _ in range(sides_num):
    #         timmy.forward(100)
    #         timmy.right(360 / sides_num)
    #
    # for sides_num in range(3, 11):
    #     timmy.pencolor(get_color())
    #     draw_shape(sides_num)

    # 2.
    # timmy.pensize(5)
    # def random_angle():
    #     angles = [0, 90, 180, 270]
    #     return angles[random.randint(0, 3)]
    #
    # for _ in range(250):
    #     timmy.setheading(random_angle())
    #     timmy.pencolor(random_color())
    #     timmy.forward(10)

    # 3.
    def draw_spyrograph(angle):
        timmy.speed("fastest")
        timmy.hideturtle()
        for _ in range(int(360 / angle)):
            timmy.pencolor(random_color())
            timmy.circle(65)
            timmy.right(10)

    draw_spyrograph(5)

    screen = turtle.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    start_app()