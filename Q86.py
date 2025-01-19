import csv

# Write a Python script to read a CSV file and print each row.
with open('/path/to/your/file.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)