from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        rand_x = random.randint(-230, 230)
        rand_y = random.randint(-230, 230)
        self.goto(rand_x, rand_y)

