# import turtle as t # drawing  all shapes
# tim = t.Turtle()
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side in range(3,11):
#     draw_shape(shape_side)
# # Draw a dashed line
# for i in range(20): # doted line
#     my_turtle.forward(10)  # move forward 10 units
#     my_turtle.penup()  # lift the pen
#     my_turtle.forward(5)  # move forward 5 units without drawing
#     my_turtle.pendown()  # put the pen back down

# def sqaure(): # it will draw squarew
#     Timmmy.forward(180)
#     Timmmy.left(90)
# sqaure()
# sqaure()
# sqaure()
# sqaure()
# Timmmy.forward(180)
# Timmmy.left(90)
# Timmmy.forward(180)
# Timmmy.left(90)
# Timmmy.forward(180)
# Timmmy.left(90)
# Timmmy.forward(180)
# Timmmy.left(90)
#
# import heroes
# import villains

import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Random Walk with Turtle")
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)  # Set turtle speed (1=slowest, 10=fastest)
t.pensize(10)

def generate_random_color():
    # Generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generate_random_color = (r,g,b)
    return generate_random_color

# basic_colors = ["black", "white", "red", "green", "blue", "yellow", "orange",
#                 "purple", "cyan", "magenta", "brown", "gray", "pink", "lime"]
# Function to move turtle in a random direction
angles = [ 0 ,90 , 180 ,270 ]
# Perform 1000 random moves
for _ in range(200):
    t.color(random.choice(generate_random_color()))
    t.setheading(random.choice(angles))
    t.forward(20)

# Keep the window open until it is closed by the user
