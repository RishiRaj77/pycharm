from turtle import Turtle , Screen
from paddle import Paddle

# Create a turtle screen
screen = Screen()
screen.setup(width=800 ,height=600)
screen.bgcolor("black")
screen.title("ping_pong")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)


screen.listen()
screen.onkey(r_paddle.go_up(),"up")
screen.onkey(l_paddle.go_down(),"down")
screen.onkey(r_paddle.go_up(),"s")
screen.onkey(l_paddle.go_down(),"w")


is_game_is_on = True
while is_game_is_on:
    screen.update()

screen.exitonclick()





