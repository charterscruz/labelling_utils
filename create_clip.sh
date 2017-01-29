#!/usr/bin/env bash

echo "The folder to use is  $1 "
echo "The video to use is  $2 "



ls $1/images

#rm $1/images/*.jpg

##
#python loadVideoResults.py ~/Dropbox/workspaces/matlab/datasets/videos_to_test/lanchaArgos_clip3.avi   $1/lanchaArgos_clip3result.txt $1/images/
#avconv -r 25 -q:v 2 -i $1/images/%08d.jpg $1/lanchaArgos_clip3.mp4
#rm "$1"/images/*.jpg

#python loadVideoResults.py ~/Dropbox/workspaces/matlab/datasets/videos_to_test/bigShipHighAlt_clip2.avi   $1/bigShipHighAlt_clip2result.txt $1/images/
avconv -r 25 -q:v 2 -i $1/images/%08d.jpg $1/bigShipHighAlt_clip2_mht_5.mp4
#rm "$1"/images/*.jpg

# TODO Need to improve this script. Not very usefull right now