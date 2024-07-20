from turtle import Turtle , Screen
from snake import Snake
import time

# Create a turtle screen
screen = Screen()
screen.setup(width=600 ,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()



