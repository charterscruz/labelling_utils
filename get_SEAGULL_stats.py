#!/usr/bin/env python
"""
This objective of this script is to get gt file's names (seagull format) and compute several stats
Ideally this might get the file's from a script (get_stats.sh)
"""

import numpy as np
import sys
import argparse
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def main(argv):

    parser = argparse.ArgumentParser()
    # Required arguments: input files.
    parser.add_argument(
        "input_results_file",
        help="Results to load"
    )
    parser.add_argument(
        "width",
        help="width of the video file"
    )
    parser.add_argument(
        "height",
        help="height of the video file"
    )

    args = parser.parse_args()

    label_file = np.loadtxt(args.input_results_file)

    print('MIN width and height:  ', np.min(label_file[:, 3]), np.min(label_file[:, 4]))
    print('MAX width and height', np.max(label_file[:, 3]), np.max(label_file[:, 4]))

    # Number fo labels
    print('number of labels', np.shape(label_file)[0])

    # Number of IDs
    print('number of Ids ', np.max(label_file[:,5]) + np.min(label_file[:,5]) + 1)

    # close to edges
    adjacent_to_left = label_file[:, 1] <= 1
    adjacent_to_top = label_file[:, 2] <= 1
    adjacent_to_right = ((label_file[:, 1] + label_file[:, 3]) >= (int(args.width))-1)
    adjacent_to_bottom = ((label_file[:, 2] + label_file[:, 4]) >= (int(args.height))-1)

    print('adjacent to top or bottom: ',  np.count_nonzero(adjacent_to_top)+np.count_nonzero(adjacent_to_bottom) )
    print('adjacent to left or right: ',  np.count_nonzero(adjacent_to_right)+np.count_nonzero(adjacent_to_left) )

    # Compute areas
    width = label_file[:,3]
    height = label_file[:,4]
    area = width * height

    # Prepare to plot areas
    hfont = {'fontname':'FreeSerif'}
    fig, ax = plt.subplots(figsize=(4,3))
    plt.hist(area, normed=True)
    plt.xlabel('area of BB', fontsize=14, )
    plt.xlabel('xlabel', **hfont)
    plt.ylabel('ylabel', **hfont)
    plt.ylabel('relative frequency', fontsize=14)
    plt.tight_layout()
    start, end = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(start, end, end /4.0))
    start, end = ax.get_ylim()
    ax.yaxis.set_ticks(np.arange(start, end, end /4.0))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))

    # Save the histogram in the same location as the ground truth file
    fig.savefig(args.input_results_file[:-7]+'.eps', format='eps', dpi=400, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main(sys.argv)

