"""Creates scatterplots of two quantities when provided with their data files

    * get_args - reads user-specified parameters
    * main     - creates a scatterplot adding titles provided by user

"""
import sys
import argparse
import matplotlib.pyplot as plt
import analysis_utils as au

sys.path.append('../data')


def get_args():
    """Handles parsing of user-specified parameters from command line

    Parameters
    ----------
    xfile : string
            The file name with the data of the x-axis for the plot
            Assumes that file is in /data directory of the repo

    yfile : string
            The file name with the data of the y-axis for the plot
            Assumes that file is in /data directory of the repo

    xlabel : string
             The x-axis title that you wish your plot to have

    ylabel : string
             The y-axis title that you wish your plot to have

    outfile : string
              The desired name for the file that will contain the created plot
              File will be stored in directory /data of the repository

    """

    parser = argparse.ArgumentParser(
            description='Reads input from command line and parses to main',
            prog='scatterplt')

    parser.add_argument('--xfile',
                        type=str,
                        help='Name of file with data for the x-axis',
                        required=True)

    parser.add_argument('--yfile',
                        type=str,
                        help='Name of file with data for the y-axis',
                        required=True)

    parser.add_argument('--xlabel',
                        type=str,
                        help='Desired label for the x-axis',
                        required=True)

    parser.add_argument('--ylabel',
                        type=str,
                        help='Desired label for the y-axis',
                        required=True)

    parser.add_argument('--outfile',
                        type=str,
                        help='Name of file to be given to created plot' +
                             'Will be stored in /data dir of the repo',
                        required=True)

    args = parser.parse_args()

    return args


def main():
    # Read user input from command line
    args = get_args()
    xfile = args.xfile
    yfile = args.yfile
    xlabel = args.xlabel
    ylabel = args.ylabel
    outfile = args.outfile

    # check that xfile can be opened and read its contents
    f = au.handle_open_txt(xfile)
    xdata = au.read_file_contents(f)

    # check that yfile can be opened and read its contents
    f = au.handle_open_txt(yfile)
    ydata = au.read_file_contents(f)

    # Create a scatterplot
    plt.scatter(xdata, ydata)

    # Set labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Save plot and clear buffer
    plt.savefig('../data/'+outfile)
    plt.clf()

    return 0


if __name__ == '__main__':
    main()
