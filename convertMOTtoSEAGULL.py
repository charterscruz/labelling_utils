#!/usr/bin/env python
"""

"""

import numpy as np
import os
import sys
import argparse
from decimal import getcontext, Decimal


def main(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_mot_file",
        help="label to load"
    )
    parser.add_argument(
        "output_seagull_file",
        help="Output seagull file."
    )

    args = parser.parse_args()

    getcontext().prec = 3


    # LABEL
    label_file = np.loadtxt(args.input_mot_file, delimiter=',')
    not_labbeled_list = []
    gt_file = open(args.output_seagull_file, 'w')

    for index in range(0,int(np.amax(label_file[:,0]))):
        print index

        # Check which lines have index "index"
        index_lookup = (label_file[:, 0] == index * np.ones_like(label_file[:, 0]))
        index_lookup = index_lookup.astype(int)

        if np.count_nonzero(index_lookup) != 0:
            # gt_file = open(args.output_seagull_file, 'w')

            print np.nonzero(index_lookup)

            for nonz_index in range(0,np.count_nonzero(index_lookup.astype(int))):

                position_to_read = int(np.nonzero(index_lookup)[0][nonz_index])
                print position_to_read

                left_number = float(label_file[position_to_read, 2])
                top_number = float(label_file[position_to_read, 3])
                width = float(label_file[position_to_read, 4])
                height =  float(label_file[position_to_read, 5])
                conf = float(label_file[position_to_read, 6])
                left = "%.2f" % left_number
                top = "%.2f" % top_number
                width = "%.2f" % width
                height = "%.2f" % height
                conf = "%.2f" % conf

                gt_file.write(str(index) + ' ' + '-1' + ' '+ str(left) + ' ' + str(top) + ' ' +  str(width) + ' '
                              + str(height) + ' ' + str(conf) + ' ' + '-1' + ' ' + '-1' + ' ' + '-1 \n')
                print str(index) + ' ' + '-1' + ' '+ str(left) + ' ' + str(top) + ' ' +  str(width) + ' '\
                      + str(height) + ' ' + str(conf) + ' ' + '-1' + ' ' + '-1' + ' ' + '-1 \n'



        elif np.count_nonzero(index_lookup) == 0:
            not_labbeled_list = np.append(not_labbeled_list, index)
            print('not_labbeled_list ', not_labbeled_list)

    gt_file.close()

if __name__ == '__main__':
    main(sys.argv)

