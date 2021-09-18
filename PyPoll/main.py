import os
import csv

# List of all of the candidates extracted from the csv 
candidate = [] 
total_votes = 0
summaryCandidateList = []


# Read in the cvs and add values to lists
election_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_csv,encoding='utf-8-sig') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header and build the candidate list
    # Keep track of the total votes in total_votes
    for row in csvreader:        
            candidate.append(row[2])
            total_votes = total_votes + 1


#Build a dict of summary candidates - candidate name and vote counts 

summaryCandidateList = list(set(candidate))
vote_counts_dict ={}
for item in summaryCandidateList:
    vote_counts_dict[item] = candidate.count(item)

# Find the winner using the max function 
max_votes = max(vote_counts_dict, key=vote_counts_dict.get)

# print the results 
print("\n")
print("------------------------------------------")
print("Election Results")
print("------------------------------------------")
print(f"Total Votes : {total_votes}")
print("------------------------------------------")
# need to add the candiate list here in a loop 
for key, value in vote_counts_dict.items():
    print(key,':', value, ' ', "{:.0%}".format(round((value/total_votes),2)))
print("------------------------------------------")
print("Winner")
print(max_votes)
print("------------------------------------------")
print("\n")
print("\n") 

output_path = os.path.join("..", "analysis", "PyPollResults.csv")

with open(output_path, 'w', newline='') as datafile:
    # Initialize csv.write
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["------------------------------------------"])
    writer.writerow(["Election Results"])
    writer.writerow(["------------------------------------------"])
    writer.writerow(["Total Votes :",total_votes])
    writer.writerow(["------------------------------------------"])
    for key, value in vote_counts_dict.items():
        writer.writerow([key,':', value,  "{:.0%}".format(round((value/total_votes),2))])
    writer.writerow(["------------------------------------------"])
    writer.writerow(["Winner"])
    writer.writerow([max_votes])
    writer.writerow(["------------------------------------------"])


