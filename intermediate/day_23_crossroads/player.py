from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset_position()
        self.is_at_finish_line = self.ycor() >= FINISH_LINE_Y

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
