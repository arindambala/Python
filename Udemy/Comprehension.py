# Day 26 - 100 Days of Code

import random

print(f"\n ---- List ^ Comprehension ----\n")

''' numerals = [1, 2, 3] # General
added = []
for num in numerals:
    add = num + 1
    added.append(add)
print(added) # [2, 3, 4]

# _list = [_item for item in list] - 1

numerals = [1, 2, 3]
added = [(num + 1) for num in numerals] # Comprehension
print(added) # [2, 3, 4]

# _list = [_item for item in list if test] - 2

names = ['Gerrard', 'Torres', 'Suarez', 'Becker', 'Salah', 'Van Dijk', 'Robertson']
kop = [name for name in names if len(name) < 8] # Conditional List Comprehension
print(kop) # ['Gerrard', 'Torres', 'Suarez', 'Becker', 'Salah'] '''

name = 'Ri'
letters = [letter for letter in name]
print(letters) # ['R', 'i']

doub = [num * 2 for num in range(1, 5)] 
print(doub) # [2, 4, 6, 8]

print(f"\n ---- Dictionary ^ Comprehension ----\n")

''' # _dict = {_key:_value for item in list} | {_key:_value for (key, value) in dict.items()} | {_key:_value for (key, value) in dict.items() if test}

players = ['Gerrard', 'Torres', 'Suarez', 'Becker', 'Salah', 'Van Dijk', 'Robertson']
scores = {rating:random.randint(1, 10) for rating in players}
print(scores) # {'Gerrard': 10, 'Torres': 6, 'Suarez': 9, 'Becker': 5, 'Salah': 10, 'Van Dijk': 3, 'Robertson': 6}

wages = {player:rating for (player, rating) in scores.items() if rating >= 7}
print(wages) # {'Becker': 9, 'Robertson': 9} '''

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()

dict = {word: len(word) for word in words}
print(dict) # {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f) # {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}