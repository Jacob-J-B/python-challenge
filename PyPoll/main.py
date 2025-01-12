# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
results = {}
dummy = 0
winner = ""
winning_votes = 0
results_text = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # main loop performing analysis
    for row in reader:
        total_votes += 1 #keep a running tally of all votees
        if row[2] not in results: #check if current candidate is NOT already a key in the dictionary results {}
            results.update({row[2]: 0}) #if not, add current candidate to results {} as a key
        results[row[2]] += 1 #now all candidates either already were a key or have been added, now increase their vote count by 1

for key, value in results.items(): #loop through results and find winner by determining who has largest vote total
    if value > winning_votes:
        winner = key #store winner name
        winning_votes = value #store winning vote total


#total vote count, format of output specified in example
output_01 = (
    "Election Results\n"
    "-------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------"
)
#winner, format specified in example
output_02 = (
    "-------------------\n"
    f"Winner: {winner}\n"
    "-------------------"
)

print(output_01) #print the total votes to the terminal 

for key, value in results.items(): #this prints each candidate and their vote count to terminal
    print(f"{key}: {float((results.get(key)/total_votes)*100):.3f}% ({value})")

print(output_02) #print the winner to the terminal

# write the results to a text file, was unable to determine how to format lines 53+54 as a string variable to print to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_01+output_02)

