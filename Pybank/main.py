# Import statements 
import os,csv

#file path
budget_file_path = os.path.join("..","Resources","budget_data.csv")

#INITIALIZE VARIABLES
# The total number of months included in the dataset
total_months = 0 

# The net total amount of "Profit/Losses" over the entire period
total_profit = 0

# The greatest increase in profits (date and amount) over the entire period
largest_increase = 0
largest_increase_date = "1/1/1970"

#initialize first value for change in profits
previous_profit = 0
current_profit = 0

#create list for dates and for change in pnl
changeInPNL =[]
changeDates =[]

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
change_total = 0.00
avg_profit = 0.00 

largest_loss_date ="1/1/1970"


with open(budget_file_path, encoding='UTF-8') as csvfile:

    #create a reader with current file
    reader_file = csv.reader(csvfile,delimiter=",")   
    
    #skip header row
    skip_header = next(reader_file)
    
    #loop to get the total number of months
    for row in reader_file:
        
        #get total number of months
        total_months+=1
        
        #holds the sum total of losses and gains
        total_profit+= round(float(row[1]))
 
           
        if previous_profit == 0:
            previous_profit = int(row[1])
        
        elif current_profit == 0:
            
            current_profit = int(row[1])
            
            change_total+=current_profit-previous_profit
            
            #add current change to list
            changeInPNL.append(current_profit-previous_profit)
            
            #populate list with corresponding dates
            changeDates.append(row[0])
            
            previous_profit = current_profit
            current_profit = 0

#close reader file            
csvfile.close()

#greatest loss  
# find min in list: https://www.tutorialspoint.com/python/list_min.htm        
largest_loss = min(changeInPNL)
findIndex = changeInPNL.index(min(changeInPNL))
largest_loss_date = changeDates[findIndex]  

#greatest increase
largest_increase = max(changeInPNL)
findIndex = changeInPNL.index(max(changeInPNL))
largest_increase_date = changeDates[findIndex]

#average change
avg_profit = round(sum(changeInPNL)/len(changeInPNL),2)

output =[]

#OUTPUT
output.append(f"Financial Analysis")
output.append(" ")
output.append("----------------------------------")
output.append(" ")
output.append(f"Total Months: {total_months}")
output.append(" ")
output.append(f"Total: ${total_profit}")
output.append(" ")
output.append(f"Average Change: ${avg_profit}")
output.append(" ")
output.append(f"Greatest Increase in Profits: {largest_increase_date} (${largest_increase})")
output.append(" ")
output.append(f"Greatest Decrease in Profits: {largest_loss_date} (${largest_loss})")


#Save results to a text file
results_path = os.path.join("..","analysis","Results.txt")   

#testing code
file = open(results_path,'w')   

#write a text file and not a csv file
#https://www.pythontutorial.net/python-basics/python-write-text-file/
for x in output:
    file.write(x)
    file.write('\n')

 
        
    

