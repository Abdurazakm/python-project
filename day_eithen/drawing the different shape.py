from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
import random

#drawing the different shape with defferent color
def change_color():
    R = random.random()
    B = random.random()
    M = random.random()

    timmy_the_turtle.color(R, M, B)


def draw_shape(num_side):
    change_color()
    for _ in range(num_side):
        angle = 360/num_side
        timmy_the_turtle.right(angle)
        timmy_the_turtle.forward(100)

for shape_side in range(3, 11):
    draw_shape(shape_side)

my_screen = Screen()
my_screen.exitonclick()