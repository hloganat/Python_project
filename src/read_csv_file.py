import csv
import argparse
import sys

global_input_file = "./input/input.csv"


def read_csv_file():
    with open(global_input_file) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            print(row)

def write_csv_file(input_file, input_data):
    with open(input_file, 'w', newline='') as csvDataFile:
        writer = csv.writer(csvDataFile)
        #writer.writerows(input)
        writer.writerows(input_data)

def read_csv_file_without_csv_module():
    file = open(global_input_file, 'r', newline='')
    file_lines = file.readlines()
    for line in file_lines:
        print(line, '\n')
    file.close()

if __name__ == "__main__":
    csv_data=[['01/01/2016', 4], ['02/01/2016', 2], ['03/01/2016', 10], ['04/01/2016', 8]]
    #write_csv_file(csv_data)
    #read_csv_file_without_csv_module()
    #read_csv_using_panda()
    #parser = argparse.ArgumentParser(description='short sample')
    #parser.add_argument('-f', default=False, dest='input_file')
    #parser.add_argument('-d', default=False, dest='input_data')
    #csv_args = parser.parse_args()
    input_file = sys.argv[1]
    #write_csv_file(csv_args.input_file, csv_data)
    write_csv_file(input_file, csv_data)
