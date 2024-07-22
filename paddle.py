
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self = Turtle()
        self.shape("sqaure")
        self.color("white")
        self.shapesize(wid=5, len=1)
        self.penup()
        self.goto(350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor() , new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor() , new_y)
