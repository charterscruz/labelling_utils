# labelling_utils
This repository contains scripts used to transform, get information, etc from labelling files and videos.

get_SEAGULL_stats.sh
This bash script is used to call get_SEAGULL_stats.sh
Input argument is a folder in which should be seagull gt files0

get_SEAGULL_stats.py
This scripts determines the minimum and maximum size of the objects in a SEAGULL gt file,
the number of frames where the object is adjacent to the edges,
the number of IDs present in the file and also
plots and histogram of area for each file

get_kitty_stats.py
Because kitty format has a gt file for each image, this scripts receives as argument a folder and not a file
This scripts determines the minimum and maximum size of the objects in Kitty gt file,
the number of frames where the object is adjacent to the edges,
the number of IDs present in the file and also
plots and histogram of area for each file

remap_seagull_labels.py
This script transforms labels that were created in one resolution to another

loadVideoResults.py 
This script takes a results file (or GT) and a video and overlays bounding boxes on images and saves these images.

loadVideoSaveImages.py
This script takes a results file (or GT) and a video and overlays bounding boxes on images and saves these images.
 
 NOTE 1: The format used for seagull GT is:
 frame_number x y width height object_id temporary/final

 NOTE 2: The format used for seagull detection is:
 frame_number x y width height object_id confidence

 TODO: Add description of KITTY format