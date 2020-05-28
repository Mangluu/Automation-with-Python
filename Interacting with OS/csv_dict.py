import csv

with open("software.csv") as soft:
    reader = csv.DictReader(soft)
    for row in reader:
        print(row["name"], row["users"])
