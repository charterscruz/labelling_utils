import cv2
import numpy as np
import argparse

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1
gx, gy = -1, -1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix, iy, drawing, mode, gx, gy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        gx, gy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img_copy,(ix, iy),(x, y),(0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        gx = x
        gy = y
        cv2.rectangle(img_copy,(ix,iy),(x,y),(0,255,0), 2)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

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

# load videos
capture = cv2.VideoCapture(args.input_video_file)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
frameCounter = 0

# Load video frame and results
ret, img = capture.read()
img_copy = img.copy()

# Check if endOfFile
if 0xFF & cv2.waitKey(1) == 27:
    cv2.destroyAllWindows()
    print "First case break"

# if frame acquisition fails for some reason
elif ret == False:
    print "Second case break"
    cv2.destroyAllWindows()
img = np.flipud(img)

# Get images properties
width, height, channels = img.shape
print width, height

while (1):
    cv2.imshow('image', img_copy)
    img_copy = img.copy()
    k = cv2.waitKey(1) & 0xFF

    if ix != -1 and iy != -1:
        cv2.rectangle(img_copy, (ix, iy), (gx, gy), (0, 255, 0), 2)

    if k == 100:
        capture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)
        ret, img = capture.read()
        img = np.flipud(img)
        img_copy = img.copy()

    elif k == 27:
        print 'exiting program'
        break

    elif k == 10 and ix != -1 and iy != -1:
        break

capture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)
# ret, img = capture.read()
# img = np.flipud(img)

print 'gx gy '
print gx, gy
print 'ix, iy'
print ix, iy
cv2.waitKey(0)

while True:
    if ix == -1 or iy == -1:
        break
    # Load video frame and results

    ret, img = capture.read()
    # img = np.flipud(img)

    # Check if endOfFile
    if 0xFF & cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        print "ESC was pressed. leaving script"
        break

    # if frame acquisition fails for some reason
    elif ret == False:
        print "frame acquisition failed"
        cv2.destroyAllWindows()
        break

    # Get images properties
    width, height, channels = img.shape

    if width == 0 or height == 0:
        print width
        print height
        cv2.destroyAllWindows()
        break

    # Crop the image

    if np.remainder(gx-ix, 2) != 0:
        gx = gx + 1
    if np.remainder(gy-iy, 2) != 0:
        iy = iy - 1

    img_crop = img[iy: gy, ix: gx ]
    print np.shape(img_crop)

    cv2.imshow('image',img_crop)
    # cv2.imshow('image', img)
    cv2.waitKey(1)
    strName= "%08i.jpg" % frameCounter
    cv2.imwrite(args.output_folder+strName, img_crop)  # ,  [int(cv2.IMWRITE_JPEG_QUALITY), 90]

    print frameCounter
    frameCounter=frameCounter+1



cv2.destroyAllWindows()

