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
    data = np.zeros((len(glob.glob('*.txt')), 2, 10000))
    data_list_w = []
    data_list_h = []
    ptr = 0
    print sorted(glob.glob('*.txt'))
    for file_ptr in sorted(glob.glob("*.txt")):

        print file_ptr
        label_file = np.loadtxt(args.input_folder + file_ptr)
        # data [ptr, :, :] = label_file[:, 3:4]
        print np.amin(label_file[:, 3])
        print np.amin(label_file[:, 4])
        data_list_w.append(np.abs(label_file[:, 3]))
        data_list_h.append((label_file[:, 4]))
        ptr = ptr + 1

    data_order = []
    data_order.append(data)

    hfont = {'fontname': 'FreeSerif'}


    fig, ax = plt.subplots(figsize=(6, 3))
    plt.xlabel('sequences', fontsize=14, )
    plt.ylabel('width', fontsize=14)
    plt.xlabel('sequences', **hfont)
    plt.ylabel('width', **hfont)
    plt.boxplot(data_list_w)

    fig.savefig('width.eps', format='eps', dpi=400, bbox_inches='tight')
    plt.show()
    plt.close()

    fig, ax = plt.subplots(figsize=(6, 3))
    plt.xlabel('sequences', fontsize=14, )
    plt.ylabel('height', fontsize=14)
    plt.xlabel('sequences', **hfont)
    plt.ylabel('height', **hfont)
    plt.boxplot(data_list_h)

    fig.savefig('height.eps', format='eps', dpi=400, bbox_inches='tight')
    plt.show()
    plt.close()

    # fig, ax = plt.subplots(figsize=(4, 3))
    # plt.hist(area, normed=True)
    # plt.xlabel('area of BB', fontsize=14, )
    # plt.ylabel('relative frequency', fontsize=14)
    # plt.xlabel('xlabel', **hfont)
    # plt.ylabel('ylabel', **hfont)
    # plt.tight_layout()
    # start, end = ax.get_xlim()
    # ax.xaxis.set_ticks(np.arange(start, end, end / 4.0))
    # start, end = ax.get_ylim()
    # ax.yaxis.set_ticks(np.arange(start, end, end / 4.0))
    # ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))
    #
    # fig.savefig('./test.eps', format='eps', dpi=400, bbox_inches='tight')
    # plt.show()

if __name__ == '__main__':
    main(sys.argv)

