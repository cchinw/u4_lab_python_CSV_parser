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
