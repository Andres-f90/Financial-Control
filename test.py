import csv
import datetime as dt
import matplotlib.pyplot as plt

file = open('expenses.csv')

csvReader = csv.reader(file)

header = []
header = next(csvReader)

dates = []
amounts = []
total = 0
for row in csvReader:
    dates.append(row[0])
    currentAmount = float(row[1][1:].replace(",", ""))
    amounts.append(currentAmount)
    total += currentAmount

print(header)
print(dates[0])
print(amounts[0])
print(total)

file.close()