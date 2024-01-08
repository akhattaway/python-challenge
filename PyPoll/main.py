import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

# Open and read the csv
with open(election_data, 'r') as csv_file:
    # Initialize csv.reader
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Read the header row
    csv_header = next(csv_reader)
    
    # Initialize variables
    voter_count = 0
    Candidates = {}
    most_votes = 0
    Winner = " "

    # Iterate through rows
    for row in csv_reader:
        # Count votes
        voter_count += 1

        # List candidates
        candidate = row[2]

        # Count votes for each candidate
        if candidate in Candidates:
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1

    # Calculate total candidate votes
    #Total_Votes = sum(Candidates.values())

print(f"Total Votes = {voter_count}")

for candidate, votes in Candidates.items():
    candidate_percentage = (votes / voter_count) * 100
    print(f"{candidate}: {votes} votes, {candidate_percentage:.3f}% of all votes")
    
for candidate, votes in Candidates.items():
    if votes > most_votes:
        most_votes = votes
        Winner = candidate
print(f"Winner: {Winner}")

file_path = os.path.join("PyPoll","analysis", "output.txt")
with open(file_path, "w") as file:
    # Write your output to the file
    file.write("Election Results\n")
    file.write("---------------------\n")
    file.write(f"Total Votes: {voter_count}\n")
    file.write("---------------------\n")
    for candidate, votes in Candidates.items():
        candidate_percentage = (votes / voter_count) * 100
        file.write(f"{candidate}: {votes} votes, {candidate_percentage:.3f}% of all votes\n")
    file.write("---------------------\n")
    file.write(f"Winner: {Winner}\n")
    file.write("---------------------\n")
