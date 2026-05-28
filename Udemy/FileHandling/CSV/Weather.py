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

data = pandas.read_csv('Weather_Data.csv')
# print(data)
print(data['TEMPERATURE'])