"""Extracts sections of a csv file when given names of desired columns and rows

    * get_args - reads user-specified parameters
    * main     - uses dataframes to extract desired sections of a csv data file
"""
import sys
import argparse
import pandas as pd
import analysis_utils as an

sys.path.append('../data')


def get_args():
    """Handles parsing of user-specified parameters from command line

    Parameters
    ----------
    filename : string
                The cvs file that contains all of the data
                Assumes that file is in /data directory of the repo

    col_title : string
                The name of the column that you need extracted (verbatim)

    country : string
              The name of the country to be extracted (verbatim)

    """

    parser = argparse.ArgumentParser(
            description='Reads input from command line and parses to main',
            prog='extract_columns')

    parser.add_argument('--filename',
                        type=str,
                        help='Name of the csv data file',
                        required=True)

    parser.add_argument('--col_title',
                        type=str,
                        help='Title of desired column as shown in csv file',
                        required=True)

    parser.add_argument('--country',
                        type=str,
                        help='The desired country as shown in csv file',
                        required=True)

    args = parser.parse_args()

    return args


def main():
    # Read user input from command line
    args = get_args()
    filename = args.filename
    col_title = args.col_title
    country = args.country

    # Read the contents of the csv file into a dataframe
    DataAll = an.handle_read_csv(filename, 'Area')

    # Extract a dataframe only containing the columns and rows specified
    DataCol = DataAll.loc[country, col_title]

    # Write dataframe to a txt file
    DataCol.to_csv('../data/'+country+'_'+col_title+'.txt', index=False)

    return 0


if __name__ == '__main__':
    main()
