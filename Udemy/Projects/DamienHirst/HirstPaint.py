# Day 18 - 100 Days of Code

# import colorgram
import turtle as turt
import random

bloom = turt.Turtle()
bloom.shape('turtle')
bloom.color('DarkOrchid')
bloom.speed('fastest')
bloom.penup()
bloom.hideturtle()
turt.colormode(255)


# rgb_colors = []
# colors = colorgram.extract('IMG_PYT.jpg', 30)
# # print(colors)

# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_set = (r, g, b)
#     rgb_colors.append(color_set)

# print(rgb_colors)

color_list = [(101, 190, 172), (103, 163, 206), (206, 137, 181), (213, 231, 241), (212, 236, 229), (61, 176, 153), (53, 123, 167), (200, 162, 107), (40, 31, 27), (238, 209, 104), (186, 91, 125), (109, 89, 76), (129, 74, 109), (161, 209, 190), (94, 125, 180), (238, 159, 181), (51, 131, 110), (58, 153, 186), (142, 209, 226), (171, 185, 221), (90, 49, 58), (187, 140, 55), (226, 174, 169), (91, 51, 45), (65, 36, 43), (32, 35, 54), (52, 56, 90), (181, 101, 89)]

bloom.setheading(225)
bloom.forward(300)
bloom.setheading(0)

dot_count = 100

for num_dot in range(1, dot_count + 1):
    bloom.dot(20, random.choice(color_list))
    bloom.forward(50)
    
    if num_dot % 10 == 0:
        bloom.setheading(90)
        bloom.forward(50)
        bloom.setheading(180)
        bloom.forward(500)
        bloom.setheading(0)

screen = turt.Screen()
screen.exitonclick()