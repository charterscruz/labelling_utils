#!/usr/bin/env python
"""

"""

import numpy as np
import sys
import argparse
import glob, os
from random import shuffle
import cv2


def main(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "label_input_folder",
        help="folder with labels to load"
    )

    parser.add_argument(
        "image_input_folder",
        help="folder with images to load"
    )

    parser.add_argument("label_output_folder", help='folder to where save the new gt')

    args = parser.parse_args()
    img_folder = args.image_input_folder
    label_folder = args.label_input_folder
    output_folder = args.label_output_folder

    # Load all labels in a folder
    os.chdir(args.label_input_folder)

    file_list = glob.glob("*.txt")

    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    max_lat = 0
    max_vert = 0

    for file_ptr in range(0, int(np.shape(file_list)[0])):

        img_name = file_list[file_ptr][:-4] + '.jpg'
        img = cv2.imread(img_folder +img_name)
        img_height, img_width, _ = img.shape
        gt = np.genfromtxt(file_list[file_ptr])

        # print file_list[file_ptr]
        np_gt = np.reshape(np.asarray(gt), (-1, 5))
        print(np_gt.shape)

        ouput_file_name = file_list[file_ptr][:-4] + '.txt'

        if np_gt.shape[0] == 1:

            print('img_height ', img_height)
            print('img_width ', img_width)
            print('int(np_gt[0, 1] * img_width): ', int(np_gt[0, 1] * img_width))
            print('int(np_gt[0, 2] * img_height): ', int(np_gt[0, 2] * img_height))

            if int(np_gt[0, 1] * img_width) > max_lat:
                max_lat = int(np_gt[0, 1] * img_width)
            if int(np_gt[0, 2] * img_height) > max_vert:
                max_vert = int(np_gt[0, 2] * img_height)

            cv2.rectangle(img,
            (int(np_gt[0, 1] * img_width), int(np_gt[0, 2] * img_height)), # top left
            (int(np_gt[0, 1] * img_width), int(np_gt[0, 2] * img_height)), # bottom right
            (0,255,0), 5)
            # cv2.imshow('image', img)
            key = cv2.waitKey(0)

            annot_to_save = [int(0), ()/float(img_width)]

        else:
            for ptr in range(0, np_gt.shape[0]):

                cv2.rectangle(img, 
                (int(np_gt[ptr, 4]), int(np_gt[ptr, 5])),
                (int(np_gt[ptr, 6]), int(np_gt[ptr, 7])), (0, 255, 0), 1)
                # cv2.imshow('image', img)
            key = cv2.waitKey(0)

        
        print(key)
        if key == 1048603:
            return 0
        print('file_ptr: ', file_ptr)
    print('max_vert: ', max_vert)
    print('max_hor: ', max_lat)

if __name__ == '__main__':
    main(sys.argv)