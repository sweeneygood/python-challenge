import os
import csv

votorid = []
county = []
candidate = []
totalVotes = 0
summaryCandidate = []
summaryCandidateVotes = []
totalCandidates = 0
i = 0


# Python has a function called 'set()' which will return a list of all unique 
# values within another list, all lists in Python also have a method called 
# 'count()' which will count all instances of a value within that list, and 
# of course there's the 'len()' function to find the total list length. 
# If you had a for-loop and a list that was just candidate names repeated for each vote...

# Read in the cvs and add values to lists
election_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_csv,encoding='utf-8-sig') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    # loop through the file and build a dict of poll results 

    for row in csvreader:        
            votorid.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
            totalVotes = totalVotes + 1

            #add the votes to the vote count for the candidate 
            #for the current candidate, if the candidate matches a candidate in the list, add 1
            # else add the candidates name to end of the summary list and add 1 to the count 

            if totalCandidates == 0: 
                summaryCandidate.append(candidate)
                summaryCandidateVotes.append(1)
                totalCandidates = totalCandidates + 1
                print(summaryCandidate)
                print(summaryCandidateVotes)
            
            else:
                print(totalCandidates)
                print(i)
                print(candidate[totalVotes-1])
                print(summaryCandidate[i])

            i = i + 1
            totalCandidates = totalCandidates + 1

                # for i in range(totalCandidates):
                #     if candidate[totalVotes-1] == summaryCandidate[i]: 
                #         summaryCandidateVotes[i] = summaryCandidateVotes[i] + 1
                #     else:
                #         summaryCandidate.append(candidate)
                #         summaryCandidateVotes.append(1)            
                #         totalCandidates = totalCandidates + 1


# print the results 
print("\n")
print("----------------------------")
print("Election Results")
print("----------------------------")
print(f"Total Votes {totalVotes}")
print("----------------------------")
print(f"Total Candidates {totalCandidates}")
print("Winner")
print("----------------------------")
print("\n")
print("\n") 