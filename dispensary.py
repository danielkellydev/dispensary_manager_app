import csv
print("Select herb to update: ")
with open("Terminal_app_assig\herb_inventory.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[1])