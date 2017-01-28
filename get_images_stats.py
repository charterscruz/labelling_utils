#!/usr/bin/env python
"""

"""

import numpy as np
import sys
import argparse
import glob, os



def main(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_folder",
        help="folder to load"
    )

    args = parser.parse_args()

    # Load all labels in a folder
    os.chdir(args.input_folder)

    min_width = 10000000000
    min_height = 10000000000

    for file_ptr in glob.glob("*.txt"):

        data = np.genfromtxt(args.input_folder + file_ptr, delimiter=' ', dtype=str)

        if (np.shape(data)) == (0,):
            pass # empty
            # print 'empty'
        elif len(np.shape(data)) == 1:
            if 0 < float(data[6]) - float(data[4]) < min_width :
                min_width = float(data[6]) - float(data[4])
            if 0 < float(data[7]) - float(data[5]) < min_height:
                min_height = float(data[7]) - float(data[5])

        else:
            for row_ptr in range(0,np.shape(data)[0]) :
                if  0 < float(data[row_ptr, 6]) - float(data[row_ptr, 4]) < min_width :
                    min_width = float(data[row_ptr, 6]) - float(data[row_ptr, 4])
                if 0 < float(data[row_ptr, 7]) - float(data[row_ptr, 5]) < min_height:
                    min_height = float(data[row_ptr, 7]) - float(data[row_ptr, 5])

    print('min_height', min_height)
    print('min_width', min_width)

    max_width = min_width
    max_height = min_height

    for file_ptr in glob.glob("*.txt"):

        data = np.genfromtxt(args.input_folder + file_ptr, delimiter=' ', dtype=str)

        if (np.shape(data)) == (0,):
            pass  # empty
            # print 'empty'
        elif len(np.shape(data)) == 1:
            if float(data[6]) - float(data[4]) > min_width:
                max_width = float(data[6]) - float(data[4])
            if float(data[7]) - float(data[5]) > min_height:
                max_height = float(data[7]) - float(data[5])

        else:
            for row_ptr in range(0, np.shape(data)[0]):
                if float(data[row_ptr, 6]) - float(data[row_ptr, 4]) > min_width:
                    max_width = float(data[row_ptr, 6]) - float(data[row_ptr, 4])
                if float(data[row_ptr, 7]) - float(data[row_ptr, 5]) > min_height:
                    max_height = float(data[row_ptr, 7]) - float(data[row_ptr, 5])

    print('max_height', max_height)
    print('max_width', max_width)

if __name__ == '__main__':
    main(sys.argv)

