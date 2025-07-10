import random
from random import choice
import colorgram
import turtle

colour = colorgram.extract("image.jpeg",9)
print(colour)

rgb_colour = []
for color in colour :
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colour.append(new_color)

print(rgb_colour)
#

color_list = [(202,23,34) , (123,67,8) , (123,34,98) , (56,78,89) , (12,34,56) ,
              (34,34,56) , (24,35,56)]
turtle.colormode(255)
tim = turtle.Turtle()
# tim.setheading(180)
# for _ in range (10):
#     tim.dot(20 , random.choice(color_list))
#     tim.forward(50)
