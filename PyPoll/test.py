#import dependencies
import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

# lists for the voting data
voter_id = []
county = []
voting_data = {}
count = 0
candidates = []
vote_count = [] # to store vote counts for each candidate
# Load and Read each file

file = os.path.join(file_path, file_name)
with open(file, newline = "") as csvfile :
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None) # skip header
    for row in csvreader :
        voter_id.append(row[0])
        candidates.append(row[2])
        voting_data[row[0]]=row[2]
# * The total number of votes cast
total_votes = len(voter_id)
# unique candidate values into a new list 'candidates_uni'
candidates_uni = list(set(candidates))
# vote count for each candidate
for i in range (len(candidates_uni)):
    for values in voting_data.values() :
        if values == candidates_uni[i]:
            count += 1
    vote_count.append(count)
    count = 0
max_vote_index = vote_count.index(max(vote_count))


# set a variable for output file.
#provide filename for the output file 
output_filename = input("Enter a file name to save the output (with extension. Ex. outputfile.txt) : ")
output_file = os.path.join(file_path, output_filename) 
with open(output_file, 'w', newline ="") as datafile: # creates an output file name in the same folder as the inputfile.
    writer  = csv.writer(datafile)
    writer.writerow(['-----------------------------------------------------------'])
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------------------------------"])
   # * The total number of votes cast 
    writer.writerow(["Total Votes: " + str(total_votes)])
    writer.writerow(["-------------------------------------------------"])
    # * A complete list of candidates who received votes
    for i in range (len(candidates_uni)):
        writer.writerow([candidates_uni[i] +": "+ str((vote_count[i]/total_votes)*100) +"%  (" + str(vote_count[i]) +")"])
    writer.writerow(["-------------------------------------------------"])
    # * The winner of the election based on popular vote.
    writer.writerow(["Winner: " + str(candidates_uni[max_vote_index])])
    writer.writerow(["-------------------------------------------------"])
    
with open(output_file, 'r', newline="")as datafile :
    reader = csv.reader(datafile, delimiter = ",")
    for row in reader:
        print(row)

print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: " + str(total_votes)")
print(f"---------------------------")
for i in range (len(candidates_uni)):
    print(f"str(candidates_uni[i]) + ":"+ str((vote_count[i]/total_votes)*100) +"%  (" + str(vote_count[i]) +")"]")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")