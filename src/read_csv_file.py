import csv

input_file = "./input/input.csv"
with open(input_file) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)