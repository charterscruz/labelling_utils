#!/usr/bin/env python
"""
This objective of this script is to look for all video files in a folder and compute several stats
Right now only the number of frames os being calculated±
"""

import numpy as np
import sys
import argparse
import glob, os
import matplotlib.pyplot as plt
import cv2

# noinspection PyInterpreter
def main(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_folder",
        help="folder to load"
    )

    args = parser.parse_args()

    # Load all labels in a folder
    os.chdir(args.input_folder)

    # Go through all the files in alphabetical order
    for file_ptr in sorted(glob.glob("*")):

        capture = cv2.VideoCapture(args.input_folder + file_ptr)

        cv2.namedWindow('test', cv2.WINDOW_NORMAL)

        frame_number = capture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
        print('file_ptr: ', file_ptr)
        print('frame_number: ', frame_number)


if __name__ == '__main__':
    main(sys.argv)

