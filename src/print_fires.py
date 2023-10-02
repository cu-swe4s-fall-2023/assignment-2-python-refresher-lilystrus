"""Finds total number of yearly fires (1990-2020) for a user-specified country

    * get_args - reads user-specified parameters
    * main     - obtains a list with the number of yearly fires
"""

import argparse
import sys
import my_utils


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
                     Path to the data file (can be relative if file in cwd)

    Keywords
    --------
    fires_column   : integer
                     The column number of the type of fires in the data file
                     Defaults to 1 (country name)

    Returns
    -------
    total_fires    : integer
                     The total number of fires for the user-specified country
                     and type of fire between years 1990 and 2020

    """
    parser = argparse.ArgumentParser(
            description='Reads input from command line and parses to main',
            prog='print_fires')

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

    parser.add_argument('--file_name',
                        type=str,
                        help='Path to the data file (can be relative)',
                        required=True)

    args = parser.parse_args()

    return args


def main():
    # Read user input from command line
    args = get_args()
    # Pass user input to a function that returns the number of yearly fires
    fires = my_utils.get_column(args.file_name, args.country_column,
                                args.country, result_column=args.fires_column)
    # Sum the yearly fires and print this total on the screen
    print("Total number of fires in " + args.country
          + " for years 1990-2020: " + str(sum(fires)))


if __name__ == '__main__':
    main()
