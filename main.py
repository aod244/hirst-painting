# import colorgram
#
# colors = colorgram.extract('image.jpg', 108)
# colors_rgb = []
#
# for color in colors:
#     color_rgb = color.rgb
#     colors_rgb.append(tuple(color_rgb))
#
import random
import turtle
from turtle import Turtle, Screen


color_list = [(34, 108, 167), (223, 229, 235), (245, 77, 36), (112, 163, 211),
 (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152),
 (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32),
 (248, 153, 143), (111, 41, 49), (155, 212, 203), (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45),
 (35, 55, 46), (99, 93, 2), (43, 151, 190), (10, 111, 51), (228, 169, 182), (177, 186, 217)]


art_turtle = Turtle()
turtle.colormode(255)
art_turtle.penup()
art_turtle.setheading(225)
art_turtle.forward(250)
art_turtle.setheading(0)
art_turtle.speed("fastest")

def hirst_painting(height, width):
    y = -176.78
    x = -176.78
    for _ in range(height):
        for _ in range(width):
            art_turtle.dot(20, random.choice(color_list))
            art_turtle.forward(50)
        y += 50
        art_turtle.setposition(x, y)


hirst_painting(10, 10)


art_screen = Screen()
art_screen.exitonclick()
