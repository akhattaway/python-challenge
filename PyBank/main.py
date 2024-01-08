import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

# Open and read the csv
with open(budget_data, 'r') as csv_file:
    # Initialize csv.reader
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Read the header row
    csv_header = next(csv_reader)
    
    # Initialize variables
    month_count = 0
    profit_losses_total = 0
    previous_profit_loss = 0
    total_change = 0
    greatest_increase = 0
    greatest_decrease = 0

    # Iterate through rows
    for row in csv_reader:
        # Count months
        month_count += 1

        # Total profit/losses
        profit_loss = float(row[1])
        profit_losses_total += profit_loss

        # Calculate change and add to total change (skip for the first row)
        if month_count > 1:
            change = profit_loss - previous_profit_loss
            total_change += change

            #set greatest increase
            if change > greatest_increase:
                greatest_increase = change

            if change < greatest_decrease:
                greatest_decrease = change 

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

    # Calculate average change stop when there are not any months left
    average_change = total_change / (month_count - 1) if month_count > 1 else 0
    
    # Save the current profit_loss for the next iteration
    previous_profit_loss = profit_loss
    
    # Print the results
    print(f"Total Months: {month_count}")
    print(f"Total Profit/Losses: {profit_losses_total}")
    print(f"Average Change: {average_change:.2f}")
    print(f"Greatest Increase: {greatest_increase}")
    print(f"Greatest Decrease: {greatest_decrease}")
