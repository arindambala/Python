# Day 5 - 100 Days of Code

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Password Generator
print(f"\n---- Welcome to Password Generator! ----")
pw_letters = int(input(f"\nHow many letters for the password? : "))
pw_numbers = int(input(f"How many numbers for the password? : "))
pw_symbols = int(input(f"How many symbols for the password? : "))

# Easy
password = ""

for char in range(0, pw_letters):
    password +=  random.choice(letters)

for char in range(0, pw_numbers):
    password += random.choice(numbers)

for char in range(0, pw_symbols):
    password += random.choice(symbols)

print(f"\n____ Generated Password: {password} ____")

# Hard
password_list = []

for char in range(0, pw_letters):
    password_list.append(random.choice(letters))

for char in range(0, pw_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, pw_symbols):
    password_list.append(random.choice(symbols))

print(f"\n{password_list}")
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"\n____ Generated Password: {password} ____")