"""Module that reads a file and extracts values based on user selections.

    * handle_file_io     - opens data file or exits on error
    * convert_str_to_int - converts data from string to integer
                           or exits on error
    * get_column         - extracts data from a file based on user selections
                           internally making use of the other two function

"""
import sys


def handle_file_io(file_name):
    """Function to open a data file or print messages on error and exit

    Parameters
    ----------
    file_name : string
                Path to the data file (can be relative if file in cwd)

    Returns
    -------
    f : file object
        Can be used outside this function for operations such as read/write

    """
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find '+file_name+'...exiting')
        sys.exit(1)
    except PermissionError:
        print('Could not open '+file_name+'...exiting')
        sys.exit(1)
    except Exception:
        print('Unknown error in opening '+filename+'...exiting')

    return f


def convert_str_to_int(Str):
    """Function to convert a string to an integer

    Parameters
    ----------
    Str : string
          The string to be converted

    Returns
    -------
    Int : integer
          The result of the conversion

    """
    try:
        Int = int(float(Str))
    except TypeError:
        print('Number of fires from data file is not of type string...exiting')
        sys.exit(1)
    except Exception:
        print('Unknown error in string to integer conversion...exiting')
        sys.exit(1)

    return Int


def get_column(file_name, query_column, query_value, result_column=1):
    """Function to extract data from a file

    Parameters
    ----------
    file_name     : string
                    The path to the data file (can be relative)

    query_column  : integer
                    The column number of the country names
                    (columns start from 1)

    query_value   : string
                    Country whose yearly fires we desire
                    e.x. 'United States of America' for the U.S.

    Keywords
    --------
    result_column : integer
                    Column number of the type of fires
                    Defaults to 1 (country name)

    Returns
    -------
    ResultList    : list of integers
                    Number of yearly fires (1990-2020)
    """
    # Initialize list that will store the number of yearly fires
    ResultList = []
    # Try to open the requested data file or exit on error
    file = handle_file_io(file_name)

    # Read file line by line and extract the requested information
    for line in file:
        # Format each line to create an array of data (1 row x columns)
        ListofLine = line.strip().split(',')
        # If the data at 'query_column'-1 of the array matches 'query_value'
        if ListofLine[query_column-1] == query_value:
            # Convert data from string to integer
            NumFiresInt = convert_str_to_int(ListofLine[result_column-1])
            # Add data to ResultList
            ResultList.append(NumFiresInt)

    file.close()

    return ResultList
