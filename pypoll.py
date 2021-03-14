# The data we need to retrive
# The total number of votes cast
# A complete list of canditates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
import csv
import os

# Assign a variable to  load a file from a  path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
# Initialize a total vote counter.
total_votes = 0

# candidate options and candidate votes
candidate_options = []
# 1.Declare empty dictonary
candidate_votes = {}

# Winning Candidate and Winning count Tracker
Winning_candidate = ""
Winning_count = 0
Winning_percentage = 0

with open(file_to_load) as election_data:
    # To do : Read and Ananlyse the data here
    # Read the file oblect with the reader function
    file_reader = csv.reader(election_data)
# Read the header row.
    headers = next(file_reader)

    for row in file_reader:
        # Add the total vote count
        total_votes += 1
    
        candidate_name = row[2]
# If the candidate does not match the existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        with open(file_to_save, "w") as txt_file:
            election_results = (
            f"\nElection results\n"
            f"---------------------------------------\n"
            f"Total Votes:  {total_votes:,}\n" 
            f"-----------------------------\n")
            print(election_results, end="")
            # save the final vote count to the text file
            txt_file.write(election_results)
        # 1. Iterate through the candidate list
        for candidate_name in candidate_votes:
            # 2. Retrive vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # 3. calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            #  Determine if the votes is greater than the winning count.
        if (votes > Winning_count) and (vote_percentage > Winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            Winning_count = votes
            Winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            Winning_candidate = candidate_name
            #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {Winning_candidate}\n"
            f"Winning Vote Count: {Winning_count:,}\n"
            f"Winning Percentage: {Winning_percentage:.1f}%\n"
            f"-------------------------\n")
    #print(winning_candidate_summary)

    # 4. print the candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage} % of the vote.")


    # print the candidate vote dictonary
    print(candidate_votes)
    # print the candidate list
    print(candidate_options)


    # print the total votes

    print(total_votes)

# Close the File.
# election_data.close()

# Using the with statement open  the file as a text file.
# with open(file_to_save,"w") as txt_file:
# Write some data to the file
#txt_file.write("Counties in the Election\n")
# txt_file.write("-------------------------\n")
# txt_file.write("Arapahoe\nDenver\nJefferson")

# Close file
# txt_file.close()
