import os
import csv

months = []
budget_per_month = []

total_months = 0 
total_amt = 0 

average_change = 0
total_change = 0

previous_amt = 0
current_amt = 0
change_amt = 0
greatest_increase_amt = 0
greatest_decrease_amt = 0
greatest_increase_month = 0
greatest_decrease_month = 0

# Need to get the csv insert part working 
# Need to fix the issue with the average change calc 

# Giving George Alonza credit for helping me with the algorithm for greatest inc/dec 

# Read in the cvs and add values to lists
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv,encoding='utf-8-sig') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    # loop through the file to calc totalMonths, totalAmt, changeAmt and averageChange
    row_num = 0

    for row in csvreader:
            # Read in the row value into variables 
            months.append(row[0])
            budget_per_month.append(int(row[1]))

            current_amt = budget_per_month[row_num-1]
        
            #determine the greatest increase and decrease amounts 
            if row_num > 1:

                change_amt = current_amt - previous_amt
                total_change = change_amt + total_change
                #print(f"change_amt {change_amt}")
                #print(f"total_change {total_change}")

                if (change_amt >= 0) and (change_amt > greatest_increase_amt):
                    greatest_increase_amt = change_amt
                    greatest_increase_month = months[row_num-1]
                    #print(f"greatest_increase_month {greatest_increase_month}")

                elif (change_amt < 0) and (change_amt < greatest_decrease_amt):
                    greatest_decrease_amt = change_amt
                    greatest_decrease_month = months[row_num-1]
                    #print(f"greatest_decrease_month {greatest_decrease_month}")

                previous_amt = current_amt
                #print(f"previous_amt {previous_amt}")

            elif row_num == 1:
                # there is no comparison needed for the first row
                previous_amt = current_amt
                #print(f"previous_amt {previous_amt}")


            # Calculate the total number of months included in the dataset
            total_months = total_months + 1
            
            # Calculate the net total amount of "Profit/Losses" over the entire period
            total_amt = total_amt + (int(row[1]))

            row_num = row_num + 1



# Calc Average Change

average_change = (total_change)/total_months

# print the results 
print("\n")
print("Financial Analysis")
print("--------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: $ {round(total_amt,2)}")
print(f"Average  Change: $ {round(average_change,2)}")
print(f"Greatest Increase in Profits: $ {greatest_increase_amt} {greatest_increase_month} ")
print(f"Greatest Decrease in Profits: $ {greatest_decrease_amt} {greatest_decrease_month} ")
print("--------------------------------------------------------")
print("\n")
print("\n")

#Export results to a file 

# Specify the file to write to
output_path = os.path.join("..", "analysis", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvoutputfile:

    # Initialize csv.write
    csvwriter = csv.writer(csvoutputfile, delimiter=',')

    # Write the output to the file 
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Months:"]) 
    csvwriter.writerow([total_months])
    csvwriter.writerow(["Total:"]) 
    csvwriter.writerow([total_amt])
    csvwriter.writerow(["Average  Change:"])
    csvwriter.writerow([round(average_change)])
    csvwriter.writerow(["Greatest Increase in Profits:"])
    csvwriter.writerow([greatest_increase_amt]) 
    csvwriter.writerow([greatest_increase_month])
    csvwriter.writerow(["Greatest Decrease in Profits:"])
    csvwriter.writerow([greatest_decrease_amt]) 
    csvwriter.writerow([greatest_decrease_month]) 
    csvwriter.writerow(["----------------------------"])

