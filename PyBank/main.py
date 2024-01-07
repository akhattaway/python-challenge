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

     # Counter variable for counting months
    month_count = 0

    # Iterate through rows
    for row in csv_reader:
        
        if row:
        # Assuming the date is in the first column, adjust if needed
            mounth_count = row[0]

        # Check if the date is not empty (assuming dates are never empty)
        if month_count:
            # Increment the month count
            month_count += 1

    # Print the total number of months
    print(f"Total Months: {month_count}")



        




