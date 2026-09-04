from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        # self.color("black")
        self.setheading(90)
        self.penup()
        # self.goto(STARTING_POSITION)
        self.goto_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)


    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)
