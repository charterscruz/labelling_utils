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
        "input_results_file_1",
        help="Results to load"
    )
    parser.add_argument(
        "input_results_file_2",
        help="Results to load"
    )
    parser.add_argument(
        "input_gt_file",
        help="GT to load"
    )
    parser.add_argument(
        "output_folder",
        help="Output folder path."
    )
    parser.add_argument(
        "save_images",
        type = int,
        help="0 -> don't save images; 1-> save images to folder."
    )

    args = parser.parse_args()

    print args.input_video_file
    print args.input_gt_file
    print args.save_images

    label_file_1 = np.loadtxt(args.input_results_file_1)
    label_file_2 = np.loadtxt(args.input_results_file_2)
    gt_file = np.loadtxt(args.input_gt_file)

    #load videos
    capture = cv2.VideoCapture(args.input_video_file)

    cv2.namedWindow('test', cv2.WINDOW_NORMAL)
    frameCounter = 0

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

        # DETECTION 1
        # Check which lines have index "index"
        dt_index_lookup_1 = (label_file_1[:, 0] == frameCounter * np.ones_like(label_file_1[:, 0]))
        dt_index_lookup_1 = dt_index_lookup_1.astype(int)

        for nonz_index in range(0, np.count_nonzero(dt_index_lookup_1.astype(int))):

            position_to_read_1 = int(np.nonzero(dt_index_lookup_1)[0][nonz_index])

            left_1 = float(label_file_1[position_to_read_1, 1]) / float(scale_x)
            top_1 = float(label_file_1[position_to_read_1, 2]) / float(scale_y)
            right_1 = (float(label_file_1[position_to_read_1, 3]) / float(scale_x) + float(label_file_1[position_to_read_1, 1]) / float(scale_x))
            bottom_1 = float(label_file_1[position_to_read_1, 2]) / float(scale_y) + float(label_file_1[position_to_read_1, 4]) / float(scale_y)
            # Draw rectangle
            cv2.rectangle(img, (int(left_1), int(top_1)), (int(right_1), int(bottom_1)), (0, 0, 255), 2)

        # DETECTION 2
        dt_index_lookup_2 = (label_file_2[:, 0] == frameCounter * np.ones_like(label_file_2[:, 0]))
        dt_index_lookup_2 = dt_index_lookup_2.astype(int)

        for nonz_index in range(0, np.count_nonzero(dt_index_lookup_2.astype(int))):
            position_to_read_2 = int(np.nonzero(dt_index_lookup_2)[0][nonz_index])

            left_2 = float(label_file_2[position_to_read_2, 1]) / float(scale_x)
            top_2 = float(label_file_2[position_to_read_2, 2]) / float(scale_y)
            right_2 = (float(label_file_2[position_to_read_2, 3]) / float(scale_x) + float(
                label_file_2[position_to_read_2, 1]) / float(scale_x))
            bottom_2 = float(label_file_2[position_to_read_2, 2]) / float(scale_y) + float(
                label_file_2[position_to_read_2, 4]) / float(scale_y)
            # Draw rectangle
            cv2.rectangle(img, (int(left_2), int(top_2)), (int(right_2), int(bottom_2)), (255, 0, 0), 2)

        # GT
        gt_index_lookup = (gt_file[:, 0] == frameCounter * np.ones_like(gt_file[:, 0]))
        gt_index_lookup = gt_index_lookup.astype(int)

        for gt_nonz_index in range(0, np.count_nonzero(gt_index_lookup.astype(int))):

            gt_position_to_read = int(np.nonzero(gt_index_lookup)[0][gt_nonz_index])

            gt_left = float(gt_file[gt_position_to_read, 1]) / float(scale_x)
            gt_top= float(gt_file[gt_position_to_read, 2]) / float(scale_y)
            gt_right = (float(gt_file[gt_position_to_read, 3]) / float(scale_x) + float(gt_file[gt_position_to_read, 1]) / float(scale_x))
            gt_bottom = float(gt_file[gt_position_to_read, 2]) / float(scale_y) + float(gt_file[gt_position_to_read, 4]) / float(scale_y)
            # Draw rectangle
            cv2.rectangle(img, (int(gt_left), int(gt_top)), (int(gt_right), int(gt_bottom)), (0, 255, 0), 2)

        # Show images
        cv2.imshow('test',img)
        cv2.waitKey(1)

        # Save images in folder specified
        if args.save_images:
            strName= "%08i.tif" % frameCounter
            cv2.imwrite(args.output_folder+strName, img)  # ,  [int(cv2.IMWRITE_JPEG_QUALITY), 90]

        print('frame number: ', frameCounter)
        frameCounter += 1

if __name__ == '__main__':
    main(sys.argv)

