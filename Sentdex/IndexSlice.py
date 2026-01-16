# Indexes & Slices
list = [1, 2, 3, 4, 5]

print(list[0]) # 1
print(list[1]) # 2
print(list[4], list[-1]) # 5 5
print(list[1:3], list[1:4]) # [2, 3] [2, 3, 4]
print(list[2:]) # [3, 4, 5]

print(list) # [1, 2, 3, 4, 5]
list[1] = 9
print(list) # [1, 9, 3, 4, 5]