import os
import csv


csv_file = os.path.join("Resources", "budget_data.csv") 
total_months = 0
total = 0
max_increase = 0
max_decrease = 0
max_date_increase = ""
max_date_decrease = ""

with open(csv_file, 'r') as file: 
    csv_reader = csv.reader(file, delimiter='\t')
    next(csv_reader)

    first_row = next(csv_reader)
    total_months = 1
    total = int(first_row[1]) 
    previous_profit = int(first_row[1])
    max_increase = 0 
    max_decrease = 0 
    
    
    for row in csv_reader:
        total_months += 1 
        record = int(row[1])
        total += record
        

        profit = int(row[1])
        difference = profit - previous_profit
        previous_profit = profit
        

        if difference > max_increase:
            max_increase = difference
            max_date_increase = row[0] 
        elif difference < max_decrease:
            max_decrease = difference
            max_date_decrease = row[0] 

average_change = (max_increase + max_decrease) / total_months
    
print("Financial Analysis") 
print("--------------------")
print(f"Total: ${total}")
print(f"Total months: {total_months}")
print("Average Change: ${:,.2f}".format(average_change))
print("Greatest Increase in Profits:", max_date_increase , "($", max_increase,")")
print("Greatest Decrease in Profits:", max_date_decrease , "($", max_decrease,")")
