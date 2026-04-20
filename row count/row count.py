import csv

row_count = 0

with open(r"C:\Users\Mridul\Downloads\python new\data.csv", "r", newline="") as file:
    reader = csv.reader(file)         # create CSV reader
    header = next(reader)             # skip header row (optional)

    for row in reader:                # loop through remaining rows
        row_count += 1
        print(row)                    # print each row if you want

print("Number of data rows:", row_count)