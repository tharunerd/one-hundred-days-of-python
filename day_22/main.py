import turtle
from paddle import Paddle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800,height=500)
screen.title("pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(l_paddle.go_up,"w")

screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    screen.update()

    
screen.exitonclick()

