# Day 10 - 100 Days of Code

#  _____________________
# |  _________________  |
# | | JO           0. | |
# | |_________________| |
# |  ___ ___ ___   ___  |
# | | 7 | 8 | 9 | | + | |
# | |___|___|___| |___| |
# | | 4 | 5 | 6 | | - | |
# | |___|___|___| |___| |
# | | 1 | 2 | 3 | | x | |
# | |___|___|___| |___| |
# | | . | 0 | = | | / | |
# | |___|___|___| |___| |
# |_____________________|

# (Regular Calculator)

# Calculator
print(f"\n---- Welcome to a Simple Calculator! ----\n")

# Operations
def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number

# Dictionary
operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
}
# print(operations['*'](3, 7)) # 21

first_number = float(input("\nWhat's the number? : "))
for symbol in operations:
    print(symbol)
calculation = input("\nChoose the required operation  (+ | - | * | /) : ")
second_number = float(input("\nWhat's the second number? : "))

result = operations[calculation](first_number, second_number)
print(f"\n____ RESULT : {first_number} {calculation} {second_number} = {result} ____")

# choice = 