from turtle import Turtle
START_POSITION = [ (0,0) , (-20,0) , (-40 , 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITION :
            new1 = Turtle("square")
            new1.color("white")
            new1.penup()
            new1.goto(position)
            self.segments.append(new1)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

