
import os

import csv

csvpath = ("C:/Users/odunz/OneDrive/Documents/python class 1,2,3/Starter_Code/PyBank/Resources/budget_data.csv")

Months =[]
Total_months = 0
Total_profit = 0
Total_Loss = []
Profit_changes = 0
List_of_changes = []
Average_Change = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

# print(csvreader) for retrival

    csv_header = next(csvreader)
    first_row = next(csvreader)
    Total_months += 1
    Total_profit += int(first_row[1])
    previous = int(first_row[1])

    for row in csvreader:
        Months.append(row[0])
        Current = int(row[1])
        Total_Loss.append(Current)
        Change = Current - previous
        Profit_changes += Change
        List_of_changes.append(Change)

# profit/loss for Total Months
        
        Total_months += 1
        Total_profit += Change
        previous = Current
# calculate the average profit/loss - total months 
    Average_Change = Profit_changes / (Total_months-1)

# Find the Greatest Max and Greatest Min
    greatest_increase = max(List_of_changes)
    greatest_decrease = min(List_of_changes)



# summary
    print('Financial Analysis')
    print('------------------------')
    print('Total Months', Total_months)
    print('Total Profit', Total_profit)
    print('Average Change', Average_Change)
    print('Greatest Profit Gain', greatest_increase)
    print('Greatest Profit Loss', greatest_decrease)


with open("financial_analysis.txt", "w") as txt_file:
    txt_file.write('Financial Analysis \n')
    txt_file.write('----------------------\n')
    txt_file.write('Total Months: ')
    txt_file.write(str(Total_months))
    txt_file.write('\nAverage Change: ')
    txt_file.write(str(Average_Change))
    txt_file.write('\nGreatest Profit Gain: ')
    txt_file.write(str(greatest_increase))
    txt_file.write('\nGreatest Profit Loss: ')
    txt_file.write(str(greatest_decrease))

