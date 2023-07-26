import os
import csv

CSV_PATH = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = []
candidates_only = []
candidates_votes = {}
percent_votes_won = 0 
total_votes_won = 0
winner = ""
winner_total = 0
name = ""



os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    #print(header)

    #for loop to check votes
    for row in csv_reader:

        #votes count
        total_votes = total_votes + 1
        name = row[2]


        #add only the new names to the new list
        if name not in candidates_only:
            candidates_only.append(name)
            candidates_votes[name] = 0

        candidates_votes[name] = candidates_votes[name] + 1
    


#display information
print("Election Results")
print("----------------------------")
print(f"Total Votes:  {total_votes}")
print("----------------------------")
for x in candidates_votes:
    votes = candidates_votes
    percent_votes_won = ((candidates_votes[x]) / total_votes) *100
    print(x + ": " + str(percent_votes_won) + "% (" + str(candidates_votes[x]) + ")")

    winner = max(candidates_votes)
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


#Display in text file 
with open('election_results.txt', 'w') as text:
    text.write("Election Results")
    text.write("----------------------------")
    text.write(f"Total Votes:  {total_votes}")
    text.write("----------------------------")
    for x in candidates_votes:
        percent_votes_won = ((candidates_votes[x]) / total_votes) *100
        text.write(x + ": " + str(percent_votes_won) + "% (" + str(candidates_votes[x]) + ")")
    text.write("-------------------------")
    text.write("The winner is: " + winner)
    text.write("-------------------------")












    