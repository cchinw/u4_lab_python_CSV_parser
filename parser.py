####################################################
#  python library imports here: csv, json

import csv
import json

####################################################
# Set up 3 global variables to process the csv file
# and convert it to JSON
# All variables will be empty lists to start: []

read_data = []
fields = []
employee_list = []

####################################################
# main function
# Takes in the path of the csv file and an output path
# for creating a new JSON file as arguments
# creates a new JSON file with formatted csv data


def csv_to_json(csv_path, json_path):
    with open(csv_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for entry in csv_data:
            read_data.append(tuple(entry))
    headers = read_data[0]
    employees = [read_data[i] for i in range(1, len(read_data))]
    for name in headers:
        fields.append(name.replace('', '_').lower())

    for employee in employees:
        employee_json = {}
        for i in range(len(employee)):
            employee_json[fields[i]] = employee[i]
        employee_list.append(employee_json)


csv_to_json('data/employee_data.csv', 'data/employees.json')
print(employee_list[2])
