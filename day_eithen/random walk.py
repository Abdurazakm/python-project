from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
import random

#random generator function
def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    timmy_the_turtle.color(R, G, B)


 
direction = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")
for _ in range(200):
    change_color()
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(direction))








my_screen = Screen()
my_screen.exitonclick()