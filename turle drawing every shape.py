import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(1)  # set the drawing speed

# Draw a red square
my_turtle.fillcolor('red')
my_turtle.begin_fill()
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
my_turtle.end_fill()

# Move to a new position and draw a blue circle
my_turtle.penup()
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.pendown()

my_turtle.fillcolor('blue')
my_turtle.begin_fill()
my_turtle.circle(50)
my_turtle.end_fill()

# Move to a new position and draw a green triangle
my_turtle.penup()
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.pendown()

my_turtle.fillcolor('green')
my_turtle.begin_fill()
for i in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)
my_turtle.end_fill()

# Move to a new position and draw a yellow rectangle
my_turtle.penup()
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.pendown()

my_turtle.fillcolor('yellow')
my_turtle.begin_fill()
for i in range(2):
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.right(90)
my_turtle.end_fill()

# Move to a new position and draw a purple pentagon
my_turtle.penup()
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.pendown()

my_turtle.fillcolor('purple')
my_turtle.begin_fill()
for i in range(5):
    my_turtle.forward(100)
    my_turtle.right(72)
my_turtle.end_fill()

# Move to a new position and draw a orange hexagon
my_turtle.penup()
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.pendown()

my_turtle.fillcolor('orange')
my_turtle.begin_fill()
for i in range(6):
    my_turtle.forward(100)
    my_turtle.right(60)
my_turtle.end_fill()

# Move to a new position and draw a brown octagon
my_turtle.penup()
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.pendown()

my_turtle.fillcolor('brown')
my_turtle.begin_fill()
for i in range(8):
    my_turtle.forward(100)
    my_turtle.right(45)
my_turtle.end_fill()

# Move to a new position and draw a pink star
my_turtle.penup()
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.pendown()

my_turtle.fillcolor('pink')
my_turtle.begin_fill()
for i in range(5):
    my_turtle.forward(100)
    my_turtle.right(144)
my_turtle.end_fill()

# Move to a new position and draw a black heart
my_turtle.penup()
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.pendown()

my_turtle.fillcolor('black')
my_turtle.begin_fill()
my_turtle.left(140)
my_turtle.forward(113)

my_turtle.circle(-90, 180)
my_turtle.setheading(60)
my_turtle.circle(-90, 180)
my_turtle.forward(112)

my_turtle.end_fill()

turtle.done()