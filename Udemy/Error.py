# Day 30 - 100 Days of Code

print(f"\n---- Error ^ Exceptions ----\n")

# TypeError
'''
text = 'abc'
print(text + 5)
'''

# IndexError
'''
fruits = ['Apple', 'Banana', 'Pear']
fruit = fruits[3]
'''

# KeyError
'''
dict = {'key': 'value'}
val = dict['non_existent']
'''

# FileNotFoundError
'''
with open('a_file.txt') as file:
    file.read()
'''

# Exception Handling

try:
    file = open('a_file.txt')
    a_dict = {'k', 'val'}
    print(a_dict['inval'])
except: #except FileNotFoundError:
    print('INVALID! No such file or directory! :")')
    # file = open('a_file.txt', 'w')
    # file.write(_data_)
# except KeyError as error:
#     print(f'{error} : non_existent')
