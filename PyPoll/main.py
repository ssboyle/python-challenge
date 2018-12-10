import os
import csv

#A copy of ""election_data.csv" is saved in my local PyBank repo folder, so I could join it directly instead of having to navigate to a different file
electiondatacsv = os.path.join("election_data.csv") 

# Read in the CSV file
with open(electiondatacsv, newline = "") as csvfile: 
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)

#Create lists:
NumVotes = []
Candidates = []
PercentageVotes = []
NumberVotes = []
Winner = []

VoterID = []
County = []
Candidate = []

for row in csvreader:
    VoterID = row[0]
    County = row[1]
    Candidate = row[2]
    print(row)



# Total number of votes cast:
# First, open csv file
with open(electiondatacsv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # ignore the header
    csv_header = next(csvreader)
    for row in csvreader:
        NumVotes.append(row[0])
    print("Total Votes" + str(len(NumVotes)))
    

# Complete list of candidates who received votes - need to loop through and grab each candidate name



# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote





