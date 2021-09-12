import os
import csv

months = []
budgetPerMonth = []
totalMonths = 0 
totalAmt = 0 
PLAmt = []
previousAmt = 0
changeAmt = []
averageChange = 0

# Read in the cvs and add values to lists
budget_csv = os.path.join("..", "Resources", "budget_data.csv")


with open(budget_csv,encoding='utf-8-sig') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    # loop through the file to calc totalMonths, totalAmt, changeAmt and averageChange

    for row in csvreader:
            months.append(row[0])
            budgetPerMonth.append(int(row[1]))
            # Calculate the total number of months included in the dataset
            totalMonths = totalMonths + 1
            print(totalMonths)
            # Calculate the net total amount of "Profit/Losses" over the entire period
            totalAmt = totalAmt + (int(row[1]))

            # Put the budget profit-loss field into a list for processing later
           # If int(totalMonths) > 2:
                #previousAmt = budgetPerMonth[0]
                #PLAmt = budgetPerMonth.[totalMonths] - previousAmt

            #if row[1] == previousAmt: 
            #print(int(row[1]).next())
            #PLAmt.append((row[1]))
            #print(PLAmt)
            #print(previousAmt)

            #changeAmt.append(rowChange)          


print(str(budgetPerMonth[5]))

# Calc Average Change
averageChange = totalAmt/totalMonths

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# print the results 
print("\n")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: {totalAmt}")
print(f"Average  Change: {averageChange}")
print(f"Greatest Increase in Profits:  ")
print(f"Greatest Decrease in Profits:  ")
print("\n")
print("\n")

#Export results to a file 

# # Specify the file to write to
# output_path = os.path.join("..", "analysis", "new.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvoutputfile:

#     # Initialize csv.writer
    # csvwriter = csv.writer(csvoutputfile, delimiter=',')

    # # Write the output to the file 
    # csvwriter.writerow(["Financial Analysis"])
    # csvwriter.writerow(["----------------------------"])
    # csvwriter.writerow([Total Months: {totalMonths}")
    # csvwriter.writerow(["Total: {totalAmt}")
    # csvwriter.writerow(["Average  Change: {averageChange}")
    # csvwriter.writerow(["Greatest Increase in Profits: Feb-2012 ($1926159) "])
    # csvwriter.writerow(["Greatest Decrease in Profits: Sep-2013 ($-2196167) "])
    

