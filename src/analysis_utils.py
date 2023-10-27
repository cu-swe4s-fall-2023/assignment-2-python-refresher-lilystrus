"""Module with various functions necessary for the analysis of correlations
   between different column/row sections of a csv file

    * handle_read_csv       - opens a csv file and handles erros in the process
    * handle_open_txt       - opens a txt file and handles erros in the process
    * read_file_contents    - reads contents of a txt file into a list
    * handle_image_open     - opens image file and handles erros in the process
    * find_final_dimensions - finds necessary width and height of an image file
                              that needs to fit multiple images in it
"""
import os
import sys
from PIL import Image, ImageDraw
import pandas as pd

sys.path.append('../data')


def handle_read_csv(filename, index_col):
    """Function to open a data file or print messages on error and exit

    Parameters
    ----------
    filename : string
                The name of the file
                Assumes it is in directory /data of repository

    index_col : string
                The title of the column for the sub-extraction that
                you will then use to narrow down the dataset to country
                Only necessary for operations that follow

    Returns
    -------
    Data : dataframe
           The data contained in the csv file

    """
    Data = None
    try:
        Data = pd.read_csv('../data/'+filename, index_col=index_col)
    except FileNotFoundError:
        print('Could not find '+filename+'in directory /data...exiting\n')
        sys.exit(1)
    except PermissionError:
        print('Could not open '+filename+'in directory /data...exiting\n')
        sys.exit(1)

    return Data


def handle_open_txt(file_name):
    """Function to open a data file or print messages on error and exit

    Parameters
    ----------
    file_name : string
                The name of the file
                Assumes it is in directory /data of repository

    Returns
    -------
    f : object
        Can be used outside this function for operations such as read/write

    """
    f = None
    try:
        f = open('../data/'+file_name, 'r')
    except FileNotFoundError:
        print('Could not find '+file_name+'in directory /data...exiting\n')
        sys.exit(1)
    except PermissionError:
        print('Could not open '+file_name+'in directory /data...exiting\n')
        sys.exit(1)
    except Exception:
        print('Error in opening '+filename+'in directory /data...exiting\n')
        sys.exit(1)

    return f


def read_file_contents(f):
    """Function to read the contents of a txt file into a list, line by line

    Parameters
    ----------
    f : object
        The object reference for the file whose contents need to be read

    Returns
    -------
    data : list
           The data contents of the file

    """
    data = []
    for line in f:
        data.append(line.strip())
    f.close()

    data = data[1:]
    data = [float(x) for x in data]
    return data


def handle_image_open(image_file):
    """Function to open an image file or print messages on error and exit

    Parameters
    ----------
    image_file : string
                 The name of the png image to be opened
                 Assumes it is in directory /data of repository
    Returns
    -------
    image_obj : object
                An image object that can be acted upon by functions
                of the Pillow module
    """
    image_obj = None
    try:
        image_obj = Image.open('../data/'+image_file)
    except FileNotFoundError:
        print('Could not find '+image_file+'in directory /data...exiting\n')
        sys.exit(1)
    except PermissionError:
        print('Could not open '+image_file+'in directory /data...exiting\n')
        sys.exit(1)

    return image_obj


def find_final_dimensions(images):
    """Computes dimensions of an image that contains multiple images

    Parameters
    ----------
    images : list
             A list of image objects that are to be combined into one file

    Returns
    -------
    width : float
            The width of the final image that will make all plots fit inside

    height : float
             The height of the final image that will make all plots fit inside
    """
    width = 0.
    height = 0.

    # get the width and height of each image
    w1, h1 = images[0].size
    w2, h2 = images[1].size
    w3, h3 = images[2].size
    w4, h4 = images[3].size

    width = 2 * max([w1, w2, w3, w4])
    height = 2 * max([h1, h2, h3, h4])

    return width, height
