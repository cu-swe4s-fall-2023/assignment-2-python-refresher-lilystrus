"""Finds total number of yearly fires (1990-2020) for a user-specified country

    * get_args - reads user-specified parameters
    * main     - obtains a list with the number of yearly fires
"""

import argparse
import sys
import my_utils
import os


def get_args():
    """Handles parsing of user-specified parameters from command line

    Parameters
    ----------
    country         : string
                      The country whose number of fires we want to find
                      e.x. type 'United States of America' for the U.S.

    country_column : integer
                     The column number of the country names in the data file
                     (columns start from 1)

    file_name      : string
                     Name of file (include extension)

    Keywords
    --------
    fires_column   : integer
                     The column number of the type of fires in the data file
                     Defaults to 1 (country name)

    Returns
    -------
    fires          : integer
                     Either the number of fires for the user-specified country
                     and type of fire for each year in 1990-2020, or
                     the mean, median or standard deviation of all yearly fires
                     between 1990 and 2020

    """
    parser = argparse.ArgumentParser(
            description='Reads input from command line and parses to main',
            prog='print_fires')

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of data file with extension',
                        required=True)

    parser.add_argument('--country',
                        type=str,
                        help='Country name e.x. United States of America',
                        required=True)

    parser.add_argument('--country_column',
                        type=int,
                        help='Column number of the country names',
                        required=True)

    parser.add_argument('--fires_column',
                        type=int,
                        help='Column number of the type of fires',
                        default=1,
                        required=False)

    parser.add_argument('--operation',
                        type=str,
                        help='The operation to perform on the fires, if any',
                        default=None,
                        required=False)

    args = parser.parse_args()

    return args


def main():
    # Read user input from command line
    args = get_args()
    file = args.file_name
    cntr = args.country
    ccol = args.country_column
    fcol = args.fires_column
    oper = args.operation

    # Start ifs for checking user input and printing the
    # Only continue if the user has given at least all required arguments
    if (file is not None and cntr is not None and ccol is not None):
        FlagCol1 = True
        if cntr is None or ccol is None:
            FlagCol1 = False
        FlagCol2 = False
        if fcol == 3 or fcol == 4:
            FlagCol2 = True
        FlagCol3 = False
        if ccol == 1:
            FlagCol3 = True
        # Only continue if column numbers are correctly supplied
        if FlagCol1 is True and FlagCol2 is True and FlagCol3 is True:
            FlagOper = False
            if oper == 'median' or oper == 'mean' or oper == 'std':
                FlagOper = True
            # Only continue if keyword operation is mean,median,std or none
            # The user did not provide any input for the operation keyword
            if oper is None and FlagOper is False:
                # Pass user input to a function that returns fires
                fires = my_utils.get_column(file, ccol, cntr,
                                            result_column=fcol,
                                            operation=oper)
                # Print the list of yearly fires
                print("Number of yearly fires in " + cntr
                      + " for years 1990-2020: " + str(fires) + '\n')
                sys.exit(1)
            # The user provided an invalid operation keyword
            elif oper is not None and FlagOper is False:
                print('Invalid input for requested operation...Exiting...\n')
                sys.exit(0)
            # The user asked for the mean of the fires
            elif oper == 'mean':
                fires = my_utils.get_column(file, ccol, cntr,
                                            result_column=fcol,
                                            operation=oper)
                print("Mean of yearly fires in " + cntr
                      + " for years 1990-2020: " + str(fires) + '\n')
                sys.exit(1)
            # The user asked for the median of the fires
            elif oper == 'median':
                fires = my_utils.get_column(file, ccol, cntr,
                                            result_column=fcol,
                                            operation=oper)
                print("Median of yearly fires in " + cntr
                      + " for years 1990-2020: " + str(fires) + '\n')
                sys.exit(1)
            # The user asked for the standard deviation of the fires
            elif oper == 'std':
                fires = my_utils.get_column(file, ccol, cntr,
                                            result_column=fcol,
                                            operation=oper)
                print("Standard Deviation of yearly fires in " + cntr
                      + " for years 1990-2020: " + str(fires) + '\n')
                sys.exit(1)
        else:
            print("Invalid input for Columns...Exiting...\n")
            sys.exit(0)
    else:
        print("You did not provide the required arguments...Exiting...\n")
        sys.exit(0)


if __name__ == '__main__':
    main()
