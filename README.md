# labelling_utils
This repository contains a scripts used to transform, get information, etc from labelling file. 

get_gt_stats.py 
This scripts determines the minimum and maximum size of the obejcts in image and also the number of frames where the object is adjacent to the edges

remap_seagull_labels.py
This script transforms labels that were created in one resolution to another

loadVideoResults.py 
This script takes a results file and a video and overlays bounding boxes on images and saves these images.
 
 NOTE: The format used fo seagull labels is:
 frame_number x y width height object_id temporary/final