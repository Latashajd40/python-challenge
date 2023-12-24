#import file
import os, csv
#I DID NOT STORE THE HEADER ROW SO, I HAVE TO DO IT FOR THIS ONE AND THE LAST ONE
election_file_path = os.path.join("..","Resources","election_data.csv")

#INITIALIZE VARIABLES
# The total number of votes cast
total_votes = 0

# A complete list of candidates who received votes
#key pair will be name:votes
candidates = []

# The percentage of votes each candidate won
percentage_won = []

# The total number of votes each candidate won
candidate_vote = 0

# The winner of the election based on popular vote
highest_vote = ""

#get unique list of candidates https://www.geeksforgeeks.org/python-get-unique-values-list/#
unique_list = []

#will hold the count for each candidate
current_count = []

#hold percentage of votes by candidate
percent_votes = []

#list holds output for terminal & print
Output = []

#read file
with open(election_file_path, encoding='UTF-8') as csvfile:

    #create a reader with current file
    reader_file = csv.reader(csvfile,delimiter=",")   
    
    #skip header row and save to variable
    skip_header = next(reader_file)
    
    for x in reader_file:
        candidates.append(x[2])
        
csvfile.close()

#add candidates to the list if they aren't
for y in candidates:
    if y not in unique_list:
        unique_list.append(y)
    
        
#count of votes per candidate
#https://www.tutorialspoint.com/How-to-count-total-number-of-occurrences-of-an-object-in-a-Python-list#:
# ~:text=Using%20the%20list%20count()%20method.%20The%20count(),we%20use%20the%20python%20count()%20method%20to

for xy in unique_list:
    current_count.append(int(candidates.count(xy)))
  
#sum of all votes
total_votes = len(candidates)

#prepare to print and save text file
#by adding data and formatting to output list
Output.append(f"Election Results")
Output.append("--------------------------")
Output.append(f"Total Votes: {total_votes}")
Output.append("--------------------------")

#calculate percentage of votes per candidate
for last in current_count:
    percent_votes.append((int(last) / int(total_votes))*100) 
   
#summary of votes by candidate
for x in range(len(current_count)):
    Output.append(f"{unique_list[x]}: {round(percent_votes[x],3)}% ({current_count[x]})")

#total number of votes for the winner     
winner_index = max(current_count)

#saving formatting and data for output    
Output.append("--------------------------")
Output.append(f"Winner: {candidates[winner_index]}")
Output.append("--------------------------")

#PRINT TO TERMINAL
for i in Output:
    print(i)
    print(" ")
 
#SAVE RESULTS TO PYPOLL_ANALYIS.TXT    
results_path = os.path.join("..","analysis","Pypoll_Analysis.txt")  

#open file w/ write permission
file = open(results_path,'w')   

#write to text file
for j in Output:
    file.write(j)
    file.write('\n')
    
file.close()
