import numpy as np
import cv2
import sys
import argparse
from itertools import islice


drawing = False # true if mouse is pressed
ix,iy = -1,-1


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)


print "Starting script..."

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

cv2.destroyAllWindows()

while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF

    if k == 10:
        mode = not mode
    elif k == 27:
        break

def main(argv):

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

    # cv2.namedWindow('test', cv2.WINDOW_NORMAL)
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

        if frameCounter == 0:
            cv2.imshow('image', img)

            while 1:
                cv2.imshow('image', img)
                k = cv2.waitKey(1) & 0xFF

                if k == 27:
                    break


        # Check which lines have index "index"

        # index_lookup = (label_file[:, 0] == frameCounter * np.ones_like(label_file[:, 0]))
        # index_lookup = index_lookup.astype(int)
        #
        # for nonz_index in range(0, np.count_nonzero(index_lookup.astype(int))):
        #
        #     position_to_read = int(np.nonzero(index_lookup)[0][nonz_index])
        #
        #     left_number = float(label_file[position_to_read, 1]) / float(scale_x)
        #     top_number = float(label_file[position_to_read, 2]) / float(scale_y)
        #     right_number = (float(label_file[position_to_read, 3]) / float(scale_x) + float(label_file[position_to_read, 1]) / float(scale_x))
        #     bottom_number = float(label_file[position_to_read, 2]) / float(scale_y) + float(label_file[position_to_read, 4]) / float(scale_y)
        #     left = left_number
        #     top =  top_number
        #     right = right_number
        #     bottom = bottom_number
        #
        #     cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), 2)
        #     # cv2.putText(img, str(label_file[position_to_read, 6])[:5], (int(right), int(top)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))


        # cv2.imshow('test',img)
        # cv2.waitKey(1)
        # strName= "%08i.tif" % frameCounter
        # cv2.imwrite(args.output_folder+strName, img)  # ,  [int(cv2.IMWRITE_JPEG_QUALITY), 90]

        print frameCounter
        frameCounter=frameCounter+1


if __name__ == '__main__':
    main(sys.argv)

