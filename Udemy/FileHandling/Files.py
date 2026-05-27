# Day 24 - 100 Days of Code

print(f"\n ---- File ^ Handling ---- \n")

# Open, Read, Write - Files | 'with' - Keyword

# file = open('Ops.txt')

''' with open('Ops.txt') as file:
    contents = file.read()
    print(contents) '''

with open('Ops.txt', mode = 'a') as file:
    file.write('\nWrite = w')

with open('New.txt', 'w') as file:
    file.write('The file has been created!')

# file.close()