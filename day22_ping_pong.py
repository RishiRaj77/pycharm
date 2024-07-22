from turtle import Turtle , Screen


# Create a turtle screen
screen = Screen()
screen.setup(width=800 ,height=600)
screen.bgcolor("black")
screen.title("ping_pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("sqaure")
paddle.color("white")
paddle.shapesize(wid=5 , len =1)
paddle.penup()
paddle.goto(350,0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor() , new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor() , new_y)


screen.listen()
screen.onkey(go_up,"up")
screen.onkey(go_down,"down")


is_game_is_on = True
while is_game_is_on:
    screen.update()

screen.exitonclick()





