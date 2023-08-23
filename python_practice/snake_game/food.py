from logging_config import game_logger
from turtle import Turtle
import random as r

HALF_SCREEN_SIZE = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
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
        game_logger.logger.debug(
            f"Refreshed, new food location: {self.position()}")

    def food_type(self):
        self.fillcolor("blue")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
