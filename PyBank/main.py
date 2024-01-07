import os
import csv
# Path to collect data from the Resources folder
budget_data = os.path.join("PyBank",'Resources', 'budget_data.csv')

# Open and read the csv
with open(budget_data, 'r') as csv_file:

    # Initialize csv.reader
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #read the header row and print header names
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

     # Counter variable -initialize variables
    month_count = 0
    profit_losses_total = 0

    # Iterate through rows
    for row in csv_reader:
        
        # count months in first column and increment 1x1
        mounth_count = row[0]
        month_count += 1

        # total profit losses over the entire period converting string to float
        profit_losses = float(row[1])
        profit_losses_total += profit_losses

        profit_losses_average = profit_losses_total/86

    # Print the total number of months
    print(f"Total Months: {month_count}")
    print(f"Total Profit/Losses, {profit_losses_total}")
    print(f"Average Profit/Losses, {profit_losses_average}")




        




