import os
import csv

file = "/Users/hyunsookim/Documents/bootcamp/Practice/homework-instructions/03_Python/python-challenge/PyBank/Resources/budget_data.csv"

with open (file,'r') as csv_file:
    budget_data = csv.reader(csv_file, delimiter=',')
    csv_header = next(budget_data)

    total_month = 0
    total = 0
    profit_list = []
    date_list = []
    profit_change_list = []

    for row in budget_data:
        total_month = total_month + 1
        total = total + int(row[1])
        profit_list.append(row[1])
        date_list.append(row[0])
    
    int_profit_list=[int (i) for i in profit_list]

    
    for j in range(len(int_profit_list) -1) :
        profit_change = int_profit_list[j+1] - int_profit_list[j] 
        profit_change_list.append(profit_change)
        
        
    len_change_list = len(profit_change_list)
    change_sum = sum(profit_change_list)
    average_change = change_sum / len_change_list

    
    greatest_increase = max(profit_change_list)
    greatest_decrease = min(profit_change_list)
    index_greatest_increase = profit_change_list.index(greatest_increase)
    index_greatest_decrese = profit_change_list.index(greatest_decrease)

result = "result.txt"
with open(result, "w") as textfile:
    
    textfile.write("Financial Analysis\n")
    textfile.write("-----------------------------------\n")
    textfile.write(f"Total months : {total_month}\n")
    textfile.write(f"Average Change : {date_list[index_greatest_increase+1]}  ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits : {date_list[index_greatest_increase+1]}   (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits : {date_list[index_greatest_decrese+1]}  (${greatest_decrease})")