#!/usr/bin/env python
"""

"""

import numpy as np
import sys
import argparse
import glob, os
from random import shuffle
import cv2
import xml.etree.ElementTree as ET


def read_content(xml_file: str):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_with_all_boxes = []

    for boxes in root.iter('object'):

        filename = root.find('filename').text

        ymin, xmin, ymax, xmax = None, None, None, None

        ymin = int(boxes.find("bndbox/ymin").text)
        xmin = int(boxes.find("bndbox/xmin").text)
        ymax = int(boxes.find("bndbox/ymax").text)
        xmax = int(boxes.find("bndbox/xmax").text)

        list_with_single_boxes = [xmin, ymin, xmax, ymax]
        list_with_all_boxes.append(list_with_single_boxes)

    return filename, list_with_all_boxes


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

    parser.add_argument(
        "label_output_folder",
        help="folder to save labels"
    )

    args = parser.parse_args()
    img_folder = args.image_input_folder
    label_folder = args.label_input_folder
    output_folder = args.label_output_folder

    # Load all labels in a folder
    os.chdir(args.label_input_folder)

    file_list = glob.glob("*.xml")

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    max_lat = 0
    max_vert = 0

    for file_ptr in range(0, int(np.shape(file_list)[0])):

        img_name = file_list[file_ptr][:-4] + '.jpg'
        try:
            img = cv2.imread(img_folder + img_name)
        except:
            print("image was not correctly loaded")
        if (img is None):
            print("image was not correctly loaded")

        img_height, img_width, _ = img.shape
        # with open(file_list[file_ptr]) as xml_file:
        #     xml_file_data = xml_file.read()
        #     dict_data = xmltodict(xml_file_data)
        name, boxes = read_content(file_list[file_ptr])
        # gt = np.genfromtxt(file_list[file_ptr])

        # print file_list[file_ptr]
        np_gt = np.reshape(np.asarray(boxes), (-1, 4))  # [xmin, ymin, xmax, ymax]
        print(np_gt.shape)


        ouput_file_name = file_list[file_ptr][:-4] + '.txt'

        if np_gt.shape[0] == 1:

            print('img_height ', img_height)
            print('img_width ', img_width)
            # print('int(np_gt[0, 1] * img_width): ', int(np_gt[0, 1] * img_width))
            # print('int(np_gt[0, 2] * img_height): ', int(np_gt[0, 2] * img_height))
            print('np_gt[0, :] ): ', np_gt[0, :])
            # print('int(np_gt[0, :] ): ', (np_gt[0, :]))
            # print('int(np_gt[0, 1] ): ', int(np_gt[0, 1]))
            # print('int(np_gt[0, 2] ): ', int(np_gt[0, 2]))
            # print('int(np_gt[0, 3] ): ', int(np_gt[0, 3]))


            cv2.rectangle(img,
            (int(np_gt[0, 0] ), int(np_gt[0, 1] )), # top left
            (int(np_gt[0, 2] ), int(np_gt[0, 3] )), # bottom right
            (0,255,0), 1)
            cv2.imshow('image', img)
            key = cv2.waitKey(1)

            #               class   x_middle    y_middle     widht   height
            annot_to_save = [int(0), 
                            (np_gt[0, 0] + np_gt[0, 2])/float(2 * img_width), 
                            (np_gt[0, 1] + np_gt[0, 3])/float(2 * img_height),
                            (np_gt[0, 2] - np_gt[0, 0])/float( img_width),
                            (np_gt[0, 3] - np_gt[0, 1])/float( img_height)]

            print('x middle', (np_gt[0, 0] + np_gt[0, 2])/float(2 * img_width)) 
            print('y middle', (np_gt[0, 1] + np_gt[0, 3])/float(2 * img_height))
            print('width', (np_gt[0, 2] - np_gt[0, 0])/float( img_width))
            print('height',(np_gt[0, 3] - np_gt[0, 1])/float( img_height))
            annot_to_save = np.reshape(annot_to_save, (1, 5))
            print('annot_to_save: ', annot_to_save)
            

        else:
            annot_to_save = np.empty(np_gt.shape[0], 5)

            for ptr in range(0, np_gt.shape[0]):

                cv2.rectangle(img, 
                (int(np_gt[ptr, 0]), int(np_gt[ptr, 1])),
                (int(np_gt[ptr, 2]), int(np_gt[ptr, 3])), (0, 255, 0), 1)
                
                annot_to_save[ptr, :] = [int(0), 
                            (np_gt[0, 0] + np_gt[0, 2])/float(2 * img_width), 
                            (np_gt[0, 1] + np_gt[0, 3])/float(2 * img_height),
                            (np_gt[0, 2] - np_gt[0, 0])/float( img_width),
                            (np_gt[0, 1] - np_gt[0, 3])/float( img_height)]

            cv2.imshow('image', img)
            key = cv2.waitKey(1)

        np.savetxt(output_folder + ouput_file_name, annot_to_save)
        print('key', key)
        if key == 1048603:
            cv2.destroyAllWindows()
            return 0

        elif key == 27:         # wait for ESC key to exit    
            cv2.destroyAllWindows()
            return 0


        print('file_ptr: ', file_ptr)
    print('max_vert: ', max_vert)
    print('max_hor: ', max_lat)

if __name__ == '__main__':
    main(sys.argv)