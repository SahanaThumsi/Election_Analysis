# The data we need to retrive
# The total number of votes cast
# A complete list of canditates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
import csv
import os
# Assign a variable to  load a file from a  path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path  
file_to_save = os.path.join("analysis","election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
# To do : Read and Ananlyse the data here
# Read the file oblect with the reader function
 file_reader = csv.reader(election_data)
# print each row in the csv file
 headers = next(file_reader)
 print(headers)
# Close the File.
#election_data.close()

#Using the with statement open  the file as a text file.
#with open(file_to_save,"w") as txt_file:
# Write some data to the file
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("-------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# Close file
# txt_file.close()

