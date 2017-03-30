#!/usr/bin/env python
"""

"""

import numpy as np
import os
import sys
import argparse
import cv2
from decimal import getcontext, Decimal
# Set precision.

def main(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_video_file",
        help="clip to load"
    )
    parser.add_argument(
        "input_label_file",
        help="label to load"
    )
    parser.add_argument(
        "output_file_prefix",
        help="Output file path."
    )

    parser.add_argument(
        "convert_video",
        help="Want to convert video (y/n ?)."
    )
    parser.add_argument(
        "width",
        help="Scale to resize images and labels."
    )
    parser.add_argument(
        "height",
        help="Scale to resize images and labels."
    )

    parser.add_argument(
        "ignore_smaller",
        help="ignore labels that are smaller than what is specified."
    )

    args = parser.parse_args()

    getcontext().prec = 3

    capture = cv2.VideoCapture(args.input_video_file)

    orig_width = capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    orig_height = capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    scale_x = float(orig_width) / float(args.width)
    scale_y = float(orig_height) / float(args.height)
    print scale_x, scale_y

    min_size = args.ignore_smaller


    # LABEL
    label_file = np.loadtxt(args.input_label_file)
    not_labbeled_list = []

    for index in range(0,int(np.amax(label_file[:,0]))):
        # print index
        # gt_file = open(args.output_file_prefix + '_' + str(index) + '.txt', 'w')

        # Check which lines have index "index"
        index_lookup = (label_file[:, 0] == index * np.ones_like(label_file[:, 0]))
        index_lookup = index_lookup.astype(int)

        if np.count_nonzero(index_lookup) != 0:
            gt_file = open(args.output_file_prefix + '_' + str(index) + '.txt', 'w')
            # pass
            # print np.nonzero(index_lookup)
            for nonz_index in range(0,np.count_nonzero(index_lookup.astype(int))):

                if min_size == 0:
                    position_to_read = int(np.nonzero(index_lookup)[0][nonz_index])

                    left_number = float(label_file[position_to_read, 1]) / float(scale_x)
                    top_number = float(label_file[position_to_read, 2])/float(scale_y)
                    right_number = (float(label_file[position_to_read, 3]) / float(scale_x) + float(label_file[position_to_read, 1]) / float(scale_x))
                    bottom_number = float(label_file[position_to_read, 2]) / float(scale_y) + float(label_file[position_to_read, 4]) / float(scale_y)
                    left = "%.2f" % left_number
                    top = "%.2f" % top_number
                    right = "%.2f" % right_number
                    bottom = "%.2f" % bottom_number

                    gt_file.write('Car' + ' ' + '0.00' + ' '+'0' + ' ' + '0.00'+' ' +  str(left)+' '+ str(top) + ' ' + str(right) + ' ' + str(bottom) + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00\n')
                #            class   truncated   occluded    alpha         left          top            right          bottom

                else:
                    position_to_read = int(np.nonzero(index_lookup)[0][nonz_index])

                    if float((label_file[position_to_read, 3])) > float(min_size) and float(label_file[position_to_read, 4]) > float(min_size):

                        left_number = float(label_file[position_to_read, 1]) / float(scale_x)
                        top_number = float(label_file[position_to_read, 2]) / float(scale_y)
                        right_number = (float(label_file[position_to_read, 3]) / float(scale_x) + float(label_file[position_to_read, 1]) / float(scale_x))
                        bottom_number = float(label_file[position_to_read, 2]) / float(scale_y) + float(label_file[position_to_read, 4]) / float(scale_y)
                        left = "%.2f" % left_number
                        top = "%.2f" % top_number
                        right = "%.2f" % right_number
                        bottom = "%.2f" % bottom_number
                        gt_file.write('Car' + ' ' + '0.00' + ' ' + '0' + ' ' + '0.00' + ' ' + str(left) + ' ' + str(top) + ' ' + str(right) + ' ' + str(
                            bottom) + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00\n')
                    else:
                        pass

            gt_file.close()

        elif np.count_nonzero(index_lookup) == 0:
            not_labbeled_list = np.append(not_labbeled_list, index)

    print('not_labbeled_list ', not_labbeled_list)

    if args.convert_video == 'y':
        # VIDEO
        # capture = cv2.VideoCapture(args.input_video_file)
        # print capture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

        for index in range(0, int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))):
            # capture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, index)
            print capture.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
            rect , img = capture.read()

            if np.any(not_labbeled_list == index * np.ones_like(not_labbeled_list)):
                pass
            else:
                img = cv2.resize(img,(int(args.width), int(args.height)))
                cv2.imwrite(args.output_file_prefix + '_' + str(index) + '.jpg', img)

if __name__ == '__main__':
    main(sys.argv)

