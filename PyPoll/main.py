import os
import csv

#A copy of ""election_data.csv" is saved in my local PyBank repo folder, so I could join it directly instead of having to navigate to a different file
electiondatacsv = os.path.join("election_data.csv") 

# Read in the CSV file
with open(electiondatacsv, newline = "") as csvfile: 
    num_votes = []
    candidates = []
    percentage_votes = []
    number_votes = []
    winner = []
    voter_id = []
    county = []
    candidate = []

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        num_votes.append(row)
    

# Total number of votes cast:

print("Total Votes" + str(len(num_votes)))


# Complete list of candidates who received votes - need to loop through and grab each candidate name


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote





