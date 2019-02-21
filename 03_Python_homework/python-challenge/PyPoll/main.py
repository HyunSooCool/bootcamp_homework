import os
import csv

file = "Resources/election_data.csv"

with open(file,"r") as csv_file:
    election_data = csv.reader(csv_file,delimiter = ',')
    csv_header = next (election_data)
    
# initate variables
    total_voter = 0
    Khan_voter = 0
    Correy_voter =0 
    Li_voter = 0
    OTooley_voter = 0
    
    for row in election_data:
        
#count total voter        
        total_voter = total_voter + 1
        
#count each candidate's voters
        if row[2] == "Khan" :
            Khan_voter = Khan_voter + 1
        elif row[2] == "Correy":
            Correy_voter = Correy_voter + 1
        elif row[2] == "Li" :
            Li_voter = Li_voter + 1
        elif row[2] == "O'Tooley" :
            OTooley_voter = OTooley_voter + 1
            
#calculate voter's percentage of each candidate
    percent_Khan = (Khan_voter*100)/total_voter
    percent_Correy = (Correy_voter*100) / total_voter
    percent_Li = (Li_voter*100) / total_voter
    percent_OTooley = (OTooley_voter*100) / total_voter
    
#find who has most voters
    candidates_list= [ "Khan","Correy","Li", "O'Tooley"]
    voter_numebr_list = [Khan_voter,Correy_voter,Li_voter, OTooley_voter]
    index_winner_candidates = voter_numebr_list.index(max(voter_numebr_list))

result = "result.txt"

with open(result, "w") as textfile:
    
    textfile.write(f"Total voter : {total_voter}\n")
    textfile.write("-----------------------------------\n")
    textfile.write(f"Khan : {int(percent_Khan)} %   ({Khan_voter})\n")
    textfile.write(f"Correy : {int(percent_Correy)}%   ({Correy_voter})\n")
    textfile.write(f"Li : {int(percent_Li)}%   ({Li_voter})\n")
    textfile.write(f"O'Tooley : {int(percent_OTooley)}%  ({OTooley_voter})\n")
    textfile.write("-----------------------------------\n")
    textfile.write(f"Winner : {candidates_list[index_winner_candidates]}\n")
    
    
    
    

