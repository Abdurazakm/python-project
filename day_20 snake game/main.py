from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=500, height=500)
screen.title("My Snake game")
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "W")
screen.onkey(snake.down, "S")
screen.onkey(snake.left, "A")
screen.onkey(snake.right, "D")



is_game_on = True
while is_game_on:
   screen.update()
   time.sleep(0.05)



   snake.move()
   #detect collision with food
   if snake.head.distance(food) < 15:
      food.refresh()
      snake.extend()
      score.increase_score()
   #detect collision with wall
   if snake.head.xcor() > 245 or snake.head.xcor() < -245 or snake.head.ycor() > 245 or snake.head.ycor() < -245:
      is_game_on = False
      score.game_over()
   #detect collision with tail
   for segment in snake.segment[1:]:#slicing method 
      if snake.head.distance(segment) < 5:
         is_game_on =  False
         score.game_over()
   





screen.exitonclick()


