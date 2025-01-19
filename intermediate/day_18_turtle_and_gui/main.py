import turtle
import random


def start_app():
    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.color("red")
    timmy.pensize(5)
    timmy.speed(10)

    color_list = [
        "light blue",
        "powder blue",
        "light gray",
        "beige",
        "light pink",
        "lavender",
        "thistle",
        "pale green",
        "honeydew",
        "mint cream",
        "light salmon",
        "misty rose",
        "peach puff",
        "blanched almond",
        "linen"
    ]

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

    def get_color():

        return color_list[random.randint(0,3)]

    # def draw_shape(sides_num):
    #     for _ in range(sides_num):
    #         timmy.forward(100)
    #         timmy.right(360 / sides_num)
    #
    # for sides_num in range(3, 11):
    #     timmy.pencolor(get_color())
    #     draw_shape(sides_num)

    def random_angle():
        angles = [0, 90, 180, 270]
        return angles[random.randint(0, 3)]

    for _ in range(50):
        timmy.setheading(random_angle())
        timmy.pencolor(get_color())
        timmy.forward(10)

    screen = turtle.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    start_app()