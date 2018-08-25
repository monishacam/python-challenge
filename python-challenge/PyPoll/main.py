# Modules
import os
import csv
#import numpy as np

total_votes = 0
candidates = {}
candidates_percentages = {}
winner_total = 0

csvpath = os.path.join("election_data.csv")

file_output = "pypollresults.txt" #will write results to this file

with open(csvpath, newline='') as csvfile:
    #set delimter of where to break data
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #read header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #calculate total votes by iterating through list and incrementing +1 with each new row
        total_votes += 1

        #create candidate dictionary where keys will be unique names, and values will be number of times they appear
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
            
        #create candidates percentages dictionary which will hold names and percent of votes for each
        for key,value in candidates.items():
            candidates_percentages[key] = round((value/total_votes)*100)
    
        #loop through percentage dictionary and keep comparing values. highest key,value pair is winner.
        for key,value in candidates_percentages.items():
            if candidates_percentages[key] > winner_total:
                winner = key
                winner_total = candidates_percentages[key]
    
#write to output file pypollresults.txt  
with open(file_output, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items(): #loop through candidates to get name, percentages, and num of votes for each
        file.write(key + ": " + str(candidates_percentages[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")   
        
        