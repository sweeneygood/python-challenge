import os
import csv

months = []
budgetPerMonth = []
totalMonths = 0 
totalAmt = 0 
changeAmt = 0
averageChange = 0

# Read in the cvs and add values to lists

budget_csv = os.path.join("..", "Resources", "budget_data.csv")


with open(budget_csv,encoding='utf-8-sig') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
            print(row)
            months.append(row[0])
            budgetPerMonth.append(row[1])
            totalMonths = totalMonths + 1
            totalAmt = totalAmt + (int(row[1]))


print(totalMonths)
print(totalAmt)


# loop through the file to calc totalMonths, totalAmt, changeAmt and averageChange

# Calculate the total number of months included in the dataset
# Calculate the net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period


# print the results 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: {totalAmt}")
print(f"Average  Change: ")
print(f"Greatest Increase in Profits:  ")
print(f"Greatest Decrease in Profits:  ")

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
    # csvwriter.writerow(["Total Months: 86"])
    # csvwriter.writerow(["Total: $38382578"])
    # csvwriter.writerow(["Average  Change: $-2315.12"])
    # csvwriter.writerow(["Greatest Increase in Profits: Feb-2012 ($1926159) "])
    # csvwriter.writerow(["Greatest Decrease in Profits: Sep-2013 ($-2196167) "])
    


