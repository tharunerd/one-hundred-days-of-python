import turtle
# from turtle import Screen , Turtle



tim = turtle.Turtle()
screen = turtle.Screen()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def move_left ():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def claer():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(claer,"c")
screen.exitonclick()

# import turtle
#
# tim = turtle.Turtle()
# screen = turtle.Screen()
#
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def move_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def move_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(move_right, "d")
# screen.onkey(move_left, "a")
# screen.onkey(clear, "c")  # Added clear function with "c" key
#
# screen.exitonclick()  # Moved to the end
