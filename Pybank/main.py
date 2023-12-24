# Import statements 
import os,csv

#file path
budget_file_path = os.path.join("..","Resources","budget_data.csv")

# The total number of months included in the dataset
total_of_months = 0

# The net total amount of "Profit/Losses" over the entire period
total_net_profit_or_loss = 0

# The greatest increase in profits (date and amount) over the entire period
highest_increase_profits = 0
highest_increase_profits_date = "1/1/1970"

#initialize first value for change in profits
profit_period_one = 0
profit_period_two = 0

#create a list of change in profits
changeInPNL =[]
changeDates =[]

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
sum_changes_profit_or_loss = 0.00
average_change_profit_or_loss = 0.00 


# The greatest decrease in profits (date and amount) over the entire period

largest_loss_date ="1/1/1970"

#skip reading the header in the data
with open(budget_file_path, encoding='UTF-8') as csvfile:

    #create a reader with current file
    reader_file = csv.reader(csvfile,delimiter=",")   
    
    #skip header row
    skip_header = next(reader_file)
    
    #loop to get the total number of months
    for row in reader_file:
        
        #get total number of months
        total_of_months+=1
        
        #holds the sum total of losses and gains
        total_net_profit_or_loss+= round(float(row[1]))
 
           
        if profit_period_one == 0:
            profit_period_one = int(row[1])
        
        elif profit_period_two == 0:
            
            profit_period_two = int(row[1])
            
            sum_changes_profit_or_loss+=profit_period_two-profit_period_one
            
            changeInPNL.append(profit_period_two-profit_period_one)
            changeDates.append(row[0])
            
            profit_period_one = profit_period_two
            profit_period_two = 0
            
largest_loss = min(changeInPNL)
findIndex = changeInPNL.index(min(changeInPNL))
largest_loss_date = changeDates[findIndex]          


#OUTPUT
print(f"Financial Analysis")
print(" ")
print("----------------------------------")
print(" ")
print(f"Total Months: {total_of_months}")
print(" ")
print(f"Total: {total_net_profit_or_loss}")
print(" ")
print(f"Average Change: {average_change_profit_or_loss}")
print(" ")
print(f"Greatest Increase in Profits: {highest_increase_profits_date} ({highest_increase_profits})")
print(" ")
print(f"Greatest Decrease in Profits: {largest_loss_date} ({largest_loss})")

