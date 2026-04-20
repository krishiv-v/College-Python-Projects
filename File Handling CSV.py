import csv

# Sample data
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 22, "Paris"]
]

# Create a new CSV file and write data
with open("people.csv", mode = "w", newline="") as file:
    writer = csv.writer(file) #create writer object and formats in CSV format
    writer.writerows(data) # write all rows at once

print("CSV file created and data written successfully!")