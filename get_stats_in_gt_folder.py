#!/usr/bin/env python
"""
This objective of this script is to look for gt files (kitty format) in a folder and compute several stats
"""

import numpy as np
import sys
import argparse
import glob, os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



def main(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_folder",
        help="folder to load"
    )

    args = parser.parse_args()

    # Load all labels in a folder
    os.chdir(args.input_folder)
    print(len(glob.glob('*.txt')))

    area = np.array(1)


    min_width = 10000000000
    min_height = 10000000000

    for file_ptr in glob.glob("*.txt"):

        data = np.genfromtxt(args.input_folder + file_ptr, delimiter=' ', dtype=str)

        if (np.shape(data)) == (0,):
            pass # empty
            # print 'empty'
        elif len(np.shape(data)) == 1:
            width = float(data[6]) - float(data[4])
            height = float(data[7]) - float(data[5])
            area = np.concatenate((np.reshape(area, (-1, 1)), np.reshape(np.array(width * height), (-1, 1))), axis=0)


            if 0 < float(data[6]) - float(data[4]) < min_width :
                min_width = float(data[6]) - float(data[4])
            if 0 < float(data[7]) - float(data[5]) < min_height:
                min_height = float(data[7]) - float(data[5])

        else:
            for row_ptr in range(0,np.shape(data)[0]) :
                width = float(data[row_ptr, 6]) - float(data[row_ptr, 4])
                height = float(data[row_ptr, 7]) - float(data[row_ptr, 5])

                area = np.concatenate((np.reshape(area, (-1,1)), np.reshape(np.array(width * height), (-1,1))), axis =0)

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

    print np.shape(area)

    hfont = {'fontname': 'FreeSerif'}

    fig, ax = plt.subplots(figsize=(4, 3))
    # plt.xticks(rotation='vertical')
    plt.hist(area, normed=True)
    plt.xlabel('area of BB', fontsize=14, )
    plt.xlabel('xlabel', **hfont)
    plt.ylabel('ylabel', **hfont)
    plt.ylabel('relative frequency', fontsize=14)
    plt.tight_layout()
    start, end = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(start, end, end / 4.0))
    start, end = ax.get_ylim()
    ax.yaxis.set_ticks(np.arange(start, end, end / 4.0))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))

    fig.savefig('./test.eps', format='eps', dpi=400, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    main(sys.argv)

