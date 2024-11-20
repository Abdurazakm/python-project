from turtle import Turtle
ALIGHMENT = "center"
FONT = ("Croureir",20,"normal")

class Scoreboard(Turtle):

    def __init__(self) :
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,220)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.write(arg=f"Score: {self.score}",move=False, align= ALIGHMENT, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",move=False, align= ALIGHMENT, font=FONT)
    def increase_score(self):
        self.clear()
        self.score+=1
        self.update()
        
        