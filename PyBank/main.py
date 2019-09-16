# Python Homework PyBank

# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`.

# Your task is to create a Python script that analyzes the records to calculate each of the following:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

# Import Modules (or is it Dependencies?)
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Setting Variables 
months = 0
net_total = 0
month_change = []
month_count = []
prev_row = 0
revenue = []

#Open budget_data.csv file
with open (csvpath) as file :
   csv_file = csv.reader(file, delimiter = ",")
    #Reading header row
   csv_header = next(csv_file)
    
# Loop through for calculations to find total months and net total amount 
   for row in csv_file:
        months += 1 
        month_count.append(row[0])
        month_change.append(int(row[1]) - prev_row)
        prev_row = int(row[1])
        revenue.append(row[1])
        net_total += int(row[1])

# Find average changes in Profit/Losses over the entire period

   average_change = (sum(month_change)-month_change[0])/(len(month_change)-1)


# find the greatest increase in profits & lowest in losses 
   greatest_increase = max(month_change)
   greatest_index = month_change.index(greatest_increase)
   greatest_month = month_count[greatest_index]

   lowest_decrease = min(month_change)
   lowest_index = month_change.index(lowest_decrease)
   lowest_month = month_count[lowest_index]


# Print Results to Terminal 
   print("Financial Analysis")
   print("------------------")
   print(f"Total Months: {str(months)}")
   print(f"Total: ${str(net_total)}")
   print(f"Average Change: ${str(round(average_change,2))}")
   print(f"Greatest Increase in Profits: {greatest_month} (${str(greatest_increase)})")
   print(f"Greatest Decrease in Profits: {lowest_month} (${str(lowest_decrease)})")

# Set Path for txt file 
output_file = os.path.join('financial_analysis.txt')

# Text File Results
with open(output_file, 'w') as txt:
    txt.write(f"Financial Analysis\n")
    txt.write(f"-------------------\n")
    txt.write(f"Total Months: {months}\n")
    txt.write(f"Total: ${net_total}\n")
    txt.write(f"Average Change: $ {str(round(average_change,2))}\n")
    txt.write(f"Greatest Increase in Profits:, {greatest_month}, (${greatest_increase})\n")
    txt.write(f"Greatest Decrease in Profits:, {lowest_month}, (${lowest_decrease})\n")