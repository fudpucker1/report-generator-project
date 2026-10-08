"""
Report Generation Functions for Flight Operations

This module contains functions for reading, processing, and reporting on
military flight operations data. Students will implement these functions
to practice file I/O, data manipulation, and report generation.
"""

import csv

def read_csv_file(filepath):
    file_data = []
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                file_data.append(row)

    except(FileNotFoundError):
        print("File not found.")
        file_data = []

    return file_data
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    # TODO: Your code here
    # Hint: Use csv.DictReader to read CSV files into dictionaries
    # Hint: Remember to use 'with open()' for proper file handling
    pass


def count_records(data_list):
    return len(data_list)
    """Counts the number of records in a dataset."""
    # TODO: Your code here
    # Hint: Use the len() function
    pass


def get_unique_values(data_list, field_name):
    data_values = []
    for row in data_list:
        data_values.append(row.get(field_name))

    return sorted(set(data_values))

    """Gets all unique values for a specific field in the dataset."""
    # TODO: Your code here
    # Hint: Use a set to collect unique values
    # Hint: Convert the set to a list and sort it before returning
    pass


def filter_by_field(data_list, field_name, field_value):
    """Filters records where a specific field matches a given value."""

    data_values = []

    for row in data_list:
        if row.get(field_name) == field_value:
            data_values.append(row)

    return data_values

    # TODO: Your code here
    # Hint: Use a list comprehension to filter or a loop!
    # see here for more info: https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions
    pass


def calculate_total(data_list, field_name):
    data_values = []
    for row in data_list:
        data_values.append(float(row.get(field_name)))

    return sum(data_values)

    """Calculates the sum of a numeric field across all records."""
    # TODO: Your code here
    # Hint: Initialize a total variable to 0
    # Hint: Loop through each record and add float(record[field_name]) to total
    # Hint: Remember to convert string values to float!
    pass


def calculate_average(data_list, field_name):
    data_values = []
    for row in data_list:
        data_values.append(float(row.get(field_name)))

    if not data_values:
        return 0

    return sum(data_values)/len(data_values)

    """Calculates the average value of a numeric field."""
    # TODO: Your code here
    # Hint: Use calculate_total() and count_records() functions
    # Hint: Average = total / count
    pass


def find_record_by_id(data_list, id_field, id_value):
    """Finds a specific record by its ID field."""
    for row in data_list:
        if row.get(id_field) == id_value:
            return row

    return None

    # TODO: Your code here
    # Hint: Loop through data_list
    # Hint: Return the record when record[id_field] == id_value
    pass


def join_data(primary_list, secondary_list, primary_key, foreign_key):
    """
    Joins two datasets together based on matching key fields.
    Similar to a SQL JOIN.
    """
    updated_list = []

    for primary_row in primary_list:
        for secondary_row in secondary_list:
            if primary_row.get(primary_key) == secondary_row.get(foreign_key):
                combined = primary_row.copy()
                combined.update(secondary_row)
                updated_list.append(combined)

    return updated_list


    # TODO: Your code here
    # Hint: Create a dictionary mapping secondary_list IDs to records
    # Hint: For each record in primary_list, look up the matching secondary record
    # Hint: Use dict.update() to merge dictionaries
    pass


def write_report_to_file(filepath, content):

    try:
        with open(filepath, 'w') as file:
            file.write(content)

    except(FileNotFoundError):
        print("File not found.")

    """Writes a text report to a file."""
    # TODO: Your code here
    # Hint: Use 'with open(filepath, 'w')' to open file for writing
    pass


def format_header(title):
    brackets = "=" * 30
    return f"{brackets} {title} {brackets}"
    """Creates a formatted header for reports."""
    # TODO: Your code here
    # Hint: Use "=" * 60 to create a line of equals signs
    # Hint: Use .center(60) to center the title
    pass


# Testing functions
if __name__ == '__main__':
    print("Testing report functions...")
    print("Implement functions above, then uncomment test code below")

    # # Test read_csv_file
    pilots = read_csv_file('../data/pilots.csv')
    print(f"Loaded {len(pilots)} pilots")
