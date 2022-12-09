import csv

FILENAME = "wimbledon.csv"

with open(FILENAME, "rt") as csvfile:
    reader = csv.reader(csvfile)
    column = [row[2] for row in reader]
    print(column)