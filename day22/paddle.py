# import turtle
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        # self = turtle.Turtle()
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
