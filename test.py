from turtle import Turtle , Screen

# Create a turtle screen
screen = Screen()
screen.setup(width=600 ,height=600)
screen.bgcolor("black")
screen.title("snake game")

starting_position = [ (0,0) , (-20,0) , (-40 , 0)]

for position in starting_position:
    new1 = Turtle("square")
    new1.color("white")
    new1.goto(position)

# Wait for the user to click to close the window
#Turtle.exitonclick()
