# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data and other necessary financial data
total_months = 0
total_net = 0
greatest_month = ""
greatest_month_profit = 0
least_month = ""
least_month_profit = 0
diff_between_months = 0
current_month = 0
last_month = 0
first_month = True
 
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # main loop to go through all rows and perform analysis
    for row in reader:
       
            total_months += 1 #keep track of total months
            total_net = total_net + int(row[1]) #keep track of the sum of all profits/loses
            if first_month == True: #the first time through there is no prior month to compare to
                last_month = int(row[1]) #capture last month to compare to next time
                first_month = False #set first month = False for all other iterations
            else:
                current_month = int(row[1])
                if (current_month - last_month) > greatest_month_profit: #determine if the current vs prior month had the largest increase
                     greatest_month_profit = current_month - last_month #if so, store value as largest_month_profit
                     greatest_month = row[0] #and store month as greatest_month
                if (current_month - last_month) < least_month_profit: #determine if the current vs prior month had the largest decrease
                     least_month_profit = current_month - last_month #if so store value as least_month_profit
                     least_month = row[0] #and store month as least_month
                diff_between_months = diff_between_months + (current_month - last_month) #keep a running tally of the difference between months
                last_month = int(row[1]) #save the current month as the last month for comparison next time through the loop
             
output = (
    "Financial Analysis\n"
    "-------------------\n"
    f"Total Months: {total_months}\n" #output total months
    f"Total: ${total_net}\n" #output net total
    f"Average Change: ${float((diff_between_months / (total_months - 1))):.2f}\n" #calculate and display average change
    f"Greatest Increase in Profits: {greatest_month} (${greatest_month_profit})\n" #display greatest increase month/amount as calculated above
    f"Greatest Decrease in Profits: {least_month} (${least_month_profit})" #display greatest decrease month/amount as caluclated above
)

#print the output to the terminal
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
