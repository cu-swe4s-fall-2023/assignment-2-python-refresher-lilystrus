"""Module that reads a file and extracts values based on user selections.

    * handle_file_io     - opens data file or exits on error
    * convert_str_to_int - converts data from string to integer
                           or exits on error
    * get_column         - extracts data from a file based on user selections
                           internally making use of the other two function

"""
import sys
import os

# sys.path.append('../data') : not working?
# found alternative
# get the current directory
cwdir = os.getcwd()
# if you are calling my_utils from test_my_utils,
# you are in /test/unit-test so ../../data
if 'unit-test' in cwdir:
    # go back two dirs
    pardir = os.path.dirname(cwdir)
    grpardir = os.path.dirname(pardir)
    # go forward one dir
    datadir = grpardir + '/data'
    # append to your path
    sys.path.append(datadir)
# if you are calling my_utils from print_fires
# you are in /src so ../data
if 'src' in cwdir:
    # go back one dir
    pardir = os.path.dirname(cwdir)
    # go forward one dir
    datadir = pardir+'/data'
    # append to your path
    sys.path.append(datadir)


def handle_file_io(file_name):
    """Function to open a data file or print messages on error and exit

    Parameters
    ----------
    file_name : string
                The name of the file (with extension)

    Returns
    -------
    f : file object
        Can be used outside this function for operations such as read/write

    """
    f = None
    try:
        f = open(datadir+'/'+file_name, 'r')
    except FileNotFoundError:
        print('Could not find '+file_name+'...exiting\n')
    except PermissionError:
        print('Could not open '+file_name+'...exiting\n')
    except Exception:
        print('Unknown error in opening '+filename+'...exiting\n')

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
    Int = None
    try:
        Int = int(float(Str))
    except TypeError:
        print('Expected variable of type string...exiting\n')
    except Exception:
        print('Unknown error in string to integer conversion...exiting\n')

    return Int


def get_column(file_name, query_column, query_value,
               result_column=1, operation=None):
    """Function to extract data from a file

    Parameters
    ----------
    file_name     : string
                    The name of the file (with extension)

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
    if file is None:
        sys.exit(1)

    # Read file line by line and extract the requested information
    for line in file:
        # Format each line to create an array of data (1 row x columns)
        ListofLine = line.strip().split(',')
        # If the data at 'query_column'-1 of the array matches 'query_value'
        if ListofLine[query_column-1] == query_value:
            # Convert data from string to integer
            NumFiresInt = convert_str_to_int(ListofLine[result_column-1])
            if NumFiresInt is None:
                sys.exit(1)
            # Add data to ResultList
            ResultList.append(NumFiresInt)

    file.close()

    if operation is None:
        return ResultList
    elif operation == 'mean':
        return find_mean(ResultList)
    elif operation == 'median':
        return find_median(ResultList)
    elif operation == 'std':
        mean = find_mean(ResultList)
        return find_std(ResultList, mean)


def valid_length(IntList):
    ListLen = len(IntList)
    dummy = None
    try:
        # If the division is not possible, ListLen has to be zero
        dummy = 1/ListLen
        dummy = ListLen
    except Exception:
        print('No entries present in the list of number of fires\n')
    finally:
        return dummy


def find_mean(IntList):
    mean = None
    ListLen = valid_length(IntList)
    if ListLen is not None:
        mean = sum(IntList)/ListLen

    return mean


def find_median(IntList):
    median = None
    ListLen = valid_length(IntList)
    if ListLen is not None:
        SortedList = sorted(IntList)
        Quotient = int(ListLen/2)
        Modulus = ListLen % 2
        # The median of a list is its 'center' number or
        # the average of its two 'center' numbers
        # It all depends on whether the length of the
        # list is an even or odd number
        if Modulus == 0:
            median = (SortedList[Quotient-1] + SortedList[Quotient])/float(2)
        else:
            median = SortedList[(ListLen+1)/2-1]

    return median


def find_std(IntList, mean):
    std = None
    ListLen = valid_length(IntList)
    if ListLen is not None:
        std = .0
        for i in range(0, ListLen-1):
            std += (IntList[i]-mean)**float(2)/(ListLen-1)
        return std**0.5
    else:
        return std
