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
    print(f"Column Headers: {csv_header}")
    
    # Initialize variables
    month_count = 0
    profit_losses_total = 0
    previous_profit_loss = 0
    total_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_date = " "
    greatest_decrease_date = " "

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

            #set greatest increase and respective date
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]

            #set greatest decrease and respective date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0] 

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

    # Calculate average change stop when there are not any months left
    average_change = total_change / (month_count - 1) if month_count > 1 else 0
    
    # Save the current profit_loss for the next iteration
    previous_profit_loss = profit_loss
    
    # Print the results
    print(f"Total Months: {month_count}")
    print(f"Total: ${profit_losses_total:.0f}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:.0f})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:.0f})")

file_path = os.path.join("PyBank","analysis", "output.txt")
with open(file_path, "w") as file:
    # Write your output to the file
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total: ${profit_losses_total:0f}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:.0f})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:.0f})\n")