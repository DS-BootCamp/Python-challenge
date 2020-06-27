import csv

with open ('Resources/budget_data.csv') as file:
    reader = csv.reader(file)

    count = 0

    for row in reader:
        print(row)