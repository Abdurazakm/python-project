import turtle as t
import random
t.colormode(255)

def random_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0,255)
    #PYTHON TUPLE
    tim.color(R, G, B)



tim = t.Turtle()
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        random_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)



my_screen = t.Screen()
my_screen.exitonclick()

   

