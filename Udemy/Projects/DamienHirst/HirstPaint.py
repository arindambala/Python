# Day 18 - 100 Days of Code

import colorgram

rgb_colors = []
colors = colorgram.extract('IMG_PYT.jpg', 30)
# print(colors)

for color in colors:
    # rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_set = (r, g, b)
    rgb_colors.append(color_set)

print(rgb_colors)

