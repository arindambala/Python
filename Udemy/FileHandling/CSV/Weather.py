# Day 25 - 100 Days of Code

# import csv
import pandas

print(f"\n---- Weather ^ Data ----\n")

# with open('Weather_Data.csv') as file:
#     data = file.readlines()
#     print(data)

''' with open('Weather_Data.csv') as file: # So much faff!
    data = csv.reader(file)
    temperatures = []
    # print(data)
    for row in data:
        # print(row)
        if row[1] != 'TEMPERATURE':
            temperatures.append(int(row[1]))
    print(temperatures) '''

# data = pandas.read_csv('Weather_Data.csv')
# print(data) - type() | DataFrame(2-D)
# print(data['TEMPERATURE']) type() | Series(1-D)

# print(data.to_dict()) - DataFrame to Dictionary
# print(data['TEMPERATURE'].to_list()) - Series to list

''' temp_list = data['TEMPERATURE'].to_list()
tot = 0
for temp in temp_list:
    tot += temp
avg_temp = tot / len(temp_list)
print(f"\nAverage Temperature | (Weekly) : {avg_temp} Celsius!") '''

# print(data['TEMPERATURE'].mean())
# print(data['TEMPERATURE'].max())

''' # Data - Columns
print(data['CONDITION'])
print(data.CONDITION) 

# Data - Rows
print(data[data.DAY == 'Monday'])
print(data[data.TEMPERATURE == data.TEMPERATURE.max()]) 

monday = data[data.DAY == 'Monday']
print(monday.CONDITION)
print(monday.TEMPERATURE[0] * (9 / 5) + 32) 

DataFrame from Scratch
dict = {
    'students': ['Ed', 'Edd', 'Eddy'],
    'scores': [75, 50, 95]
}
data = pandas.DataFrame(dict)
# print(data)
data.to_csv('Ops.csv') '''

# Central Park Squirrel Count NYC 2018
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_NYC.csv')

grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
print(grey_squirrels_count)

cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
print(cinnamon_squirrels_count)

black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(black_squirrels_count)

# squirrels_count = grey_squirrels_count + cinnamon_squirrels_count + black_squirrels_count
# print(squirrels_count)

dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
squirrels_count = pandas.DataFrame(dict)
squirrels_count.to_csv('squirrel_count.csv')