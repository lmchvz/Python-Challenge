# Python Homework PyPoll

# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won 
    # The winner of the election based on popular vote.

# Import Dependencies
import os
import csv
    
# Set path for File
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Setting Variables 
ttl_votes = 0
candidate = ""
votes = {}
candidate_pct ={}
winner_votes = 0
winner_name = ""

# Open CSV file: election_data.csv
with open(csvpath,'r') as csvfile:
    csv_file = csv.reader(csvfile, delimiter = ',')
# Reading header row to move on to next row 
    header = next(csv_file, None)

# Find the total number of votes cast
    for row in csv_file:
        ttl_votes = ttl_votes + 1
        candidate = row[2]
        
        if candidate in votes:
            votes[candidate] = votes[candidate] + 1
       
        else:
            votes[candidate] = 1

# Find the Percentage of Votes and Winner
    for name, vote_count in votes.items():
        candidate_pct[name] = '{0:.2%}'.format(vote_count / ttl_votes)
        if vote_count > winner_votes:
            winner_votes = vote_count
            winner_name = name


# Print Results to Terminal 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {ttl_votes}")
print("-------------------------")
for name, vote_count in votes.items():
    print(f"{name}: {candidate_pct[name]} ({vote_count})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

# Set Path for Text File 
output_file = os.path.join('election_results.txt')

# Write Results to Text File 
with open(output_file, 'w') as txt:
    txt.write(f"Election Results \n")
    txt.write(f"-------------------------\n")
    txt.write(f"Total Votes: {ttl_votes}\n")
    txt.write(f"-------------------------\n")
    for name, vote_count in votes.items():
        txt.write(f"{name}: {candidate_pct[name]} ({vote_count})\n")
    txt.write(f"-------------------------\n")
    txt.write(f"Winner: {winner_name}\n")
    print("-------------------------")
