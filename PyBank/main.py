import os
import csv

#A copy of "budget_data.csv is saved in my local PyBank repo folder, so I could join it directly instead of having to navigate to a different file
budgetdatacsv = os.path.join("budget_data.csv") 

# Read in the CSV file
with open(budgetdatacsv, "r") as csvfile: 
    bankdata = []  #creates a placeholder for data
    profits = []  
    avg_change = []
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        bankdata.append(row)
        profits.append(int(row[1]))

    
   
# Calculate the total number of months included included in the data set #(len(  
print(len(bankdata)) 

# The total net amount "Profit/Losses" over the entire period
#define column 1 as integer
print(sum(profits))


# The average change in "Profit/Losses" between months over the entire period *Find the change each month, then average of the changes
#Loop through the Profits to find changes:
for n in range(len(profits) -1):
    avg_change.append(profits[n+1]-profits[n])

print(sum(avg_change) / len(avg_change))


# The greatest increase in profit (date and amount) over the entire period
print(max(avg_change))

# The greatest decrease in losses (date and amount) over the entire period
print(min(avg_change))












