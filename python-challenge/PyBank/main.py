# Modules
import os
import csv
import numpy as np


total_months = 0
net_profit_loss = 0
average_change = 0
change = 0
prev_change = 0
change_list = []
month_of_change = []

csvpath = os.path.join("budget_data.csv")

file_output = "pybankresults.txt" #will write results to this file

with open(csvpath, newline='') as csvfile:
    #set delimter of where to break data
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #read header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_months += 1
        net_profit_loss += int(row[1])
        
        #calculate the average change
        change = int(row[1]) - (prev_change)
        prev_change = int(row[1])
        change_list.append(change)
        month_of_change.append(row[0])
    
    del change_list[0]    
    average_change = sum(change_list)/len(change_list)
    greatest_increase = max(change_list) #get greatest profit increase
    greatest_decrease = min(change_list) #get greatest profit decrease
    greatest_month_of_inc = month_of_change[np.argmax(change_list) + 1] #which month had greatest increase
    greatest_month_of_dec = month_of_change[np.argmin(change_list) + 1] #which month had greatest decrease
    
    #print all values calculated
    print("Total months: " + " " + str(total_months)) 
    print("Total: " + " " + str(net_profit_loss)) 
    print("Average Change: " + " " + str(average_change)) 
    print("Greatest increase in profits: " + " " + (str(greatest_month_of_inc) + " " + str(greatest_increase))) 
    print("Greatest decrease in profits: " + " " + (str(greatest_month_of_dec) + " " + str(greatest_decrease)))
    
    
    #write results to pybankresults.txt
    with open(file_output, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("---------------------\n")
        file.write("Total Months: %d\n" % total_months)
        file.write("Total: $%d\n" % net_profit_loss)
        file.write("Average Change $%d\n" % average_change)
        file.write("Greatest Increase in Profit: %s ($%s)\n" % (greatest_month_of_inc, greatest_increase))
        file.write("Greatest Decrease in Profit: %s ($%s)\n" % (greatest_month_of_dec, greatest_decrease))
    
    