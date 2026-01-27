# Day 6 - 100 Days of Code

# Reeborg's World - https://rb.gy/zg2im5 | Website
print(f"\n---- Welcome to Escape the Maze! ----")

# Robot 
def turn_right():
    for _ in range(3):
        turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


print(f"\n____ Please go to the actual webiste to try out the code! ____")