import os
import csv

csv_file = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = {}
winner = ""

with open(csv_file, 'r') as file: 
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1 
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1 
        else: 
            candidates[candidate] = 1 

percentages = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    percentages[candidate] = round(percentage, 3)

max_votes = max(candidates.values())
for candidate, votes in candidates.items():
    if votes == max_votes:
        winner= candidate
        break

print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate, votes in candidates.items():
    percentage = percentages[candidate]
    print(f"{candidate}: {percentage}% ({votes})")
print("--------------------------------")
print(f"Winner: {winner}")
print("-------------------------")