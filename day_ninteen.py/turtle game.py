from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet= screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x=-230
y=-100
all_turtle = []
for list_index in range(6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[list_index])
    new_turtle.goto(x,y)
    y+=30
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won, {winner_color} The turtle is winner")
            else:
                print(f"You've lost, {winner_color} The turtle is winner")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()