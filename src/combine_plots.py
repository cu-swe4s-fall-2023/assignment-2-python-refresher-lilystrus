"""This program accepts multiple image files and combines them into one file

    * get_args - reads user-specified parameters
    * main     - combines files when provided final image dimensions
                 and adds a title to the final image
"""
import sys
import argparse
# Image can combine images that have been created outside this .py
from PIL import Image, ImageDraw, ImageFont
import analysis_utils as au

sys.path.append('../data')


def get_args():
    """Handles parsing of user-specified parameters from command line

    Parameters
    ----------
    p1 : string
         Name of first image file to include
         Assumes that file is in /data directory of the repo

    p2 : string
         Name of first image file to include
         Assumes that file is in /data directory of the repo

    p3 : string
         Name of first image file to include
         Assumes that file is in /data directory of the repo

    p4 : string
         Name of first image file to include
         Assumes that file is in /data directory of the repo

    title : string
            Title to be used for the final plot

    outfile : string
              Name of final image file
              Will be placed in /data dir of the repo
    """

    parser = argparse.ArgumentParser(
            description='Reads input from command line and parses to main',
            prog='combine_plots')

    parser.add_argument('--p1',
                        type=str,
                        help='First image file to be included in single file',
                        required=True)

    parser.add_argument('--p2',
                        type=str,
                        help='Second image file to be included in single file',
                        required=True)

    parser.add_argument('--p3',
                        type=str,
                        help='Third image file to be included in single file',
                        required=True)

    parser.add_argument('--p4',
                        type=str,
                        help='Fourth image file to be included in single file',
                        required=True)

    parser.add_argument('--title',
                        type=str,
                        help='The title for the combined plot',
                        required=True)

    parser.add_argument('--outfile',
                        type=str,
                        help='Filename for the combined plot',
                        required=True)

    args = parser.parse_args()

    return args


def main():
    # Read user input from command line
    args = get_args()
    p1 = args.p1
    p2 = args.p2
    p3 = args.p3
    p4 = args.p4
    title = args.title
    outfile = args.outfile

    # open the images to be combined
    image1 = au.handle_image_open(p1)
    image2 = au.handle_image_open(p2)
    image3 = au.handle_image_open(p3)
    image4 = au.handle_image_open(p4)

    images = [image1, image2, image3, image4]

    # create dimensions of final image so it fits all images
    width, height = au.find_final_dimensions(images)

    # initialize object for the new image
    combined_image = Image.new('RGB', (width, height))

    # put the individual images into the final one
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (int(width/2), 0))
    combined_image.paste(image3, (0, int(height/2)))
    combined_image.paste(image4, (int(width/2), int(height/2)))

    # save final image and clear image buffer
    combined_image.save(outfile)

    return 0


if __name__ == '__main__':
    main()
