''' 
This module provides functions for creating a series of project folders. 
'''

# Import moduldes from standard library
import pathlib
import time
import os

# Import local modules
import utils_trent

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    for year in range(start_year, end_year + 1):
        year_path = project_path.joinpath(str(year))
        year_path.mkdir(exist_ok = True)
        print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")


def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders for a list of names.

    Arguments: folder_names -- The list of folder names to be created
    '''
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")
        os.makedirs(folder_name, exist_ok = True)
        print(f"FUNCTION CALLED: create_folders_from_list with '{folder_name}'")
    

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders from a list of names
    
    Arguments: folder_list -- A list of folder names to be created
    '''
    for folder_name in folder_list:
        # Create the new folder name with the prefix
        new_folder_name = f"{prefix}{folder_name}"
        os.makedirs(new_folder_name, exist_ok = True)
        print(f"CREATED FOLDER: {new_folder_name}")


def create_folders_periodically(folder_count: int, duration_seconds: int) -> None:
    # Name for the folders
    reg_name = "folder"

    created_folders = 0

    while created_folders < folder_count:
        folder_name = f"{reg_name}_{created_folders + 1}"
        os.makedirs(folder_name, exist_ok = True)
        print(f"CREATED FOLDER: {folder_name}")
    
        created_folders += 1

        if created_folders < folder_count:
            time.sleep(duration_seconds)


def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_trent.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    create_folders_periodically(folder_count = 3, duration_seconds = 5)
 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


if __name__ == '__main__':
    main()