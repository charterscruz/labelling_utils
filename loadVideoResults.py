#!/usr/bin/env python
"""
The purpose of this script is to load a video and the corresponding GT file (or detection file)
and to save images with overlay on top to a given folder
"""
import numpy as np
import cv2
import sys
import argparse
from itertools import islice


print "Starting script..."


def main(argv):
#    pycaffe_dir = os.path.dirname(__file__)

    parser = argparse.ArgumentParser()
    # Required arguments: input and output files.
    parser.add_argument(
        "input_video_file",
        help="Video to load"
    )
    parser.add_argument(
        "input_results_file",
        help="Resuts to load"
    )
    parser.add_argument(
        "output_folder",
        help="Output folder path."
    )

    args = parser.parse_args()

    print args.input_video_file

    label_file = np.loadtxt(args.input_results_file)

    #load videos
    capture = cv2.VideoCapture(args.input_video_file)

    cv2.namedWindow('test', cv2.WINDOW_NORMAL)
    frameCounter=0

    capture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frameCounter)

    scale_x = 1
    scale_y = 1

    while True:
        # Load video frame and results
        ret, img = capture.read()

        # Check if endOfFile
        if 0xFF & cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            print "Error or ESC pressed"
            break

        # if frame acquisition fails for some reason
        elif ret==False:
            print "No more frames to load"
            cv2.destroyAllWindows()
            break

        # Get images properties
        width, height, channels =img.shape

        if width == 0 or height == 0:
            print('width or height = 0 ', width, height)
            print('exiting')
            cv2.destroyAllWindows()
            break

        # Check which lines have index "index"
        index_lookup = (label_file[:, 0] == frameCounter * np.ones_like(label_file[:, 0]))
        index_lookup = index_lookup.astype(int)

        for nonz_index in range(0, np.count_nonzero(index_lookup.astype(int))):

            position_to_read = int(np.nonzero(index_lookup)[0][nonz_index])

            left = float(label_file[position_to_read, 1]) / float(scale_x)
            top= float(label_file[position_to_read, 2]) / float(scale_y)
            right = (float(label_file[position_to_read, 3]) / float(scale_x) + float(label_file[position_to_read, 1]) / float(scale_x))
            bottom = float(label_file[position_to_read, 2]) / float(scale_y) + float(label_file[position_to_read, 4]) / float(scale_y)
            # Draw rectangle
            cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), 2)

        # Show images
        cv2.imshow('test',img)
        cv2.waitKey(1)
        # Save images in folder specified
        # strName= "%08i.tif" % frameCounter
        strName= "%08i.jpg" % frameCounter
        # cv2.imwrite(args.output_folder+strName, img)  # TIF
        cv2.imwrite(args.output_folder+strName, img,  [int(cv2.IMWRITE_JPEG_QUALITY), 90]) # JPEG

        print('frame number: ', frameCounter)
        frameCounter=frameCounter+1


if __name__ == '__main__':
    main(sys.argv)

