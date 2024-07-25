from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
import time

# Create a turtle screen
screen = Screen()
screen.setup(width=800 ,height=600)
screen.bgcolor("black")
screen.title("ping_pong")
screen.tracer(0)

r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))
ball = Ball ()


screen.listen()
screen.onkey(r_paddle.go_up(),"up")
screen.onkey(l_paddle.go_down(),"down")
screen.onkey(r_paddle.go_up(),"s")
screen.onkey(l_paddle.go_down(),"w")


is_game_is_on = True
while is_game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    if ball.ycor() > 300 or ball.ycor()< -300:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 or ball.xcor() > 340 or ball.distance(l_paddle)< 50 or ball.xcor() > -340 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() > -380:
        ball.reset_position()

screen.exitonclick()
