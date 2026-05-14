# Day 16 - 100 Days of Code

from turtle import Turtle, Screen # import turtle
from prettytable import PrettyTable

# Procedural Programming || Object Oriented Programming (OOP)
print(f"\n---- Object Oriented Programming ----\n")

bloom = Turtle() # bloom = turtle.Turtle()
# print(bloom)
bloom.shape('turtle') # Icon
bloom.color('DarkOrchid') # Icon Colour 
bloom.forward(100) # Distance X-axis

# Classes & Objects
# Class - Blueprint / Template to create objects || Object - Instance of a class

scr = Screen()
# print(scr.canvheight)
scr.exitonclick()

table = PrettyTable()
# print(table)
table.add_column('Pokemon : Name', ['Bulbasaur', 'Squirtle', 'Charmander'])
table.add_column('Pokemon : Type', ['Grass', 'Water', 'Fire'])
# print(table)
table.align = 'l'
print(table)