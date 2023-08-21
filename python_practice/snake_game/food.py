from turtle import Turtle
import random as r

HALF_SCREEN_SIZE = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food_count = 0
        self.food_type()
        self.penup()
        self.speed = "fastest"
        x = r.randint(-HALF_SCREEN_SIZE, HALF_SCREEN_SIZE)
        y = r.randint(-HALF_SCREEN_SIZE, HALF_SCREEN_SIZE)
        self.goto(x, y)

        self.refresh()

    def refresh(self):
        new_x = r.randint(-HALF_SCREEN_SIZE, HALF_SCREEN_SIZE)
        new_y = r.randint(-HALF_SCREEN_SIZE, HALF_SCREEN_SIZE)
        self.food_type()
        self.goto(new_x, new_y)
        self.food_count += 1

    def food_type(self):
        if self.food_count >= 1 and self.food_count % 5 == 0:
            self.shape("turtle")
            self.fillcolor("red")
            self.shapesize(stretch_len=1, stretch_wid=1)
        else:
            self.fillcolor("blue")
            self.shape("circle")
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
