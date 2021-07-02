import csv
import math

with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def find_mean(data):
    total_entries = len(data)
    total = 0

    for x in data:
        total += int(x)
    
    mean = total / total_entries
    return mean

squared_list = []

for num in data:
    a = int(num) - find_mean(data)
    a = a ** 2
    squared_list.append(a)

b = 0

for number in squared_list:
    b = b + number

length = len(data)
result = b / (length - 1)
standard_deviation = math.sqrt(result)
print("Standard Deviation is " + str(standard_deviation))