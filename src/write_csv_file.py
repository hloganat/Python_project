import csv

global_input_file = "./input/input.csv"

def write_csv_file():
    with open(input_file, 'w', newline='') as csvDataFile:
        writer = csv.writer(csvDataFile)
        writer.writerows(csvDataFile)