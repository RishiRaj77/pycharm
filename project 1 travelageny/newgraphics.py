import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Random Walk with Turtle")
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)  # Set turtle speed (1=slowest, 10=fastest)

# Function to move turtle in a random direction
def random_move():
    # Generate a random angle between 0 and 360 degrees
    angle = random.random() * 360
    t.setheading(angle)  # Set the turtle's heading to the random angle
    t.forward(20)  # Move the turtle forward by 20 units

# Perform 1000 random moves
for _ in range(1000):
    random_move()

# Keep the window open until it is closed by the user
turtle.done()
