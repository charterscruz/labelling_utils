"""
The objective of this script is to load a video and save it as images in a folder
This does NOT consider detections or Ground truth files
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
        "output_folder",
        help="Output folder path."
    )

    args = parser.parse_args()

    print args.input_video_file

    #load videos
    capture = cv2.VideoCapture(args.input_video_file)

    cv2.namedWindow('test', cv2.WINDOW_NORMAL)
    frameCounter=0

    capture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frameCounter)

    print capture
    scale_x = 1
    scale_y = 1
    min_size = 0

    while True:
        # Load video frame and results
        ret, img = capture.read()

        # Check if endOfFile
        if 0xFF & cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            print "First case break"
            break

        # if frame acquisition fails for some reason
        elif ret==False:
            print "Second case break"
            cv2.destroyAllWindows()
            break

        # Get images properties
        width, height, channels =img.shape

        if width == 0 or height == 0:
            print width
            print height
            cv2.destroyAllWindows()
            break

        cv2.imshow('test',img)
        cv2.waitKey(1)
        strName= "%08i.tif" % frameCounter
        cv2.imwrite(args.output_folder+strName, img)  # ,  [int(cv2.IMWRITE_JPEG_QUALITY), 90]

        print frameCounter
        frameCounter=frameCounter+1


if __name__ == '__main__':
    main(sys.argv)

