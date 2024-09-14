'''
This project emphasizes skills in using Git for version control, creating and managing Python 
virtual environments, and handling different types of data. The project involves fetching data 
from the web, processing it using appropriate Python collections, and writing the processed 
data to files.
'''

# Standard library imports
import csv
import pathlib 
import json

# External library imports (requires virtual environment)
import requests
import pandas as pd

# Local module imports
import utils_trent      
import trent_project_setup

#################################
# Define fetch and write functions
#################################

def fetch_and_write_txt_data(folder_name, filename, url):
    try: 
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
    except requests.RequestException as e:
        print(f"Failed to fetch text data: {e}")

def fetch_and_write_csv_data(folder_name, filename, url):
    try: 
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
    except requests.RequestException as e:
        print(f"Failed to fetch CSV data: {e}")

def fetch_and_write_excel_data(folder_name, filename, url):
    try: 
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
    except requests.RequestException as e:
        print(f"Failed to fetch excel data: {e}")

def fetch_and_write_json_data(folder_name, filename, url):
    try: 
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
    except requests.RequestException as e:
        print(f"Failed to fetch JSON data: {e}")

###############################
# Define write functions
###############################

def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', encoding = 'utf-8') as file:
            file.write(data)
        print(f"Text data saved to {file_path}")
    except IOError as e:
        print(f"Error writing text file {file_path}: {e}")

def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', encoding = 'utf-8') as file:
            file.write(data)
        print(f"CSV data saved to {file_path}")
    except IOError as e:
        print(f"Error writing CSV file {file_path}: {e}")

def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w') as file:
            file.write(data)
        print(f"Excel data saved to {file_path}")
    except IOError as e:
        print(f"Error writing Excel file {file_path}: {e}")

def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', encoding = 'utf-8') as file:
            json.dump(data, file, indent = 4)
        print(f"JSON data saved to {file_path}")
    except IOError as e:
        print(f"Error writing JSON file {file_path}: {e}")

########################################
# Define process functions
########################################

def process_txt_file(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        with file_path.open('r', encoding = 'utf-8') as file:
            text = file.read()
    except IOError as e:
        print(f"Error reading text file {file_path}: {e}")

    try:
        # Basic processing
        words = text.lower().split()
        unique_words = set(words)
        word_count = len(words)
        unique_word_count = len(unique_words)

        # Save the results
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding = 'utf-8') as file:
            file.write(f"Total words: {word_count}\n")
            file.write(f"Unique words: {unique_word_count}\n")
        print(f"Text data processed and results saved to {output_path}")
    except Exception as e: 
        print(f"Error processing text data: {e}")

def process_csv_file(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        row_count = 0
        column_summaries = []
        data = []

        with file_path.open('r', encoding = 'utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            column_summaries = ['Column summary:'] + headers

            # Count rows
            for row in reader:
                row_count += 1 
                data.append(tuple(row))

        # Summarize columns
        column_counts = [0] * len(headers)
        for row in data:
            for i, value in enumerate(row):
                if value:
                    column_counts[i] += 1
        
        # Save the results
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding = 'utf-8') as file:
            file.write(f"Total rows: {row_count}\n")
            file.write(f"\nColumn summaries:\n")
            for header, count in zip(headers, column_counts):
                file.write(f"{header}: {count} entries\n")
        print(f"CSV data processed and results saved to {output_path}")
    except IOError as e:
        print(f"Error reading or writing CSV file: {e}")
    except csv.Error as e:
        print(f"Error processing CSV data: {e}")

def process_excel_file(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        df = pd.read_excel(file_path)
        summary = {
            'Total rows': len(df),
            'Total columns': len(df.columns),
            'Column names': list(df.columns),
            'Numeric column statistics': df.describe().to_string()
        }

        # Save the results
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding = 'utf-8') as file:
            file.write(f"Summary of excel data:\n")
            for key, value in summary.items():
                if isinstance(value, str):
                    file.write(f"{key}:\n{value}\n\n")
                else:
                    file.write(f"{key}: {value}\n")
        print(f"Excel data processed and results saved to {output_path}")
    except IOError as e:
        print(f"Error reading Excel file {file_path}: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Excel file is empty or not readable: {file_path}")
    except pd.errors.ExcelFileError as e:
        print(f"Error reading Excel file {file_path}: {e}")

def process_json_file(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        with file_path.open('r', encoding = 'utf-8') as file:
            json_data = json.load(file)

        # Summarize the data
        summary = {'Number of items': len(json_data)}

        if isinstance(json_data, list) and len(json_data) > 0 and isinstance(json_data[0], dict):
            summary['Keys in JSON objects'] = list(json_data[0].keys())
        
        # Save the results
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding = 'utf-8') as file:
            file.write(f"Summary of JSON data:\n")
            for key, value in summary.items():
                if isinstance(value, str):
                    file.write(f"{key}:\n{value}\n\n")
                else:
                    file.write(f"{key}: {value}\n")
        print(f"JSON data processed and results saved to {output_path}")
    except IOError as e:
        print(f"Error reading JSON file {file_path}: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")

###########################
# Define main function
###########################
def main():
    ''' Main function to demonstrate module capabilities. '''

    print(f"Byline: {utils_trent.byline}")

    prefix = 'data-'

    folder_names = ['txt', 'csv', 'excel', 'json']

    result = trent_project_setup.create_prefixed_folders(folder_names, prefix)
    print(result)

    base_directory = pathlib.Path(__file__).parent.joinpath('data')

    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    json_url = 'http://api.open-notify.org/astros.json'

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    txt_folder_name = pathlib.Path(base_directory).joinpath(f'{prefix}txt')
    csv_folder_name = pathlib.Path(base_directory).joinpath(f'{prefix}csv')
    excel_folder_name = pathlib.Path(base_directory).joinpath(f'{prefix}excel')
    json_folder_name = pathlib.Path(base_directory).joinpath(f'{prefix}json')

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')

#############################
# Conditional execution
#############################

if __name__ == '__main__':
    main()