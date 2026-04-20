import json, csv

# Step 1: Load JSON data
with open(r"C:\Users\Mridul\Downloads\python new\data.json", "r") as json_file:
    data = json.load(json_file) # reads and converts it into list of dictionaries

# Step 2: Create CSV file and write data
with open(r"C:\Users\Mridul\Downloads\python new\data.csv", mode = "w", newline="") as csv_file:
    # Define CSV columns (keys from JSON)
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()            # write column headers
    writer.writerows(data)          # write all rows at once

print("JSON has been converted to CSV successfully!")