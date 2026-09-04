from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

        # self.shape("square")
        # self.color(random.choice(COLORS))
        # self.turtlesize(stretch_wid=1, stretch_len=2)
        # self.penup()
        # self.speed = STARTING_MOVE_DISTANCE
        # self.goto(0, 0)

    # def car_move(self):
    #     new_x = self.xcor() + self.speed
    #     self.goto(new_x, self.ycor())
    #
    def level_up(self):
        self.speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)


