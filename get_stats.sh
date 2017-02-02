#!/usr/bin/env bash

echo $1

ls $1

dirs=$1
cd $1
for dir in $dirs
do
  echo "Directory: $dir"
  for filename in $(ls $dir)
  do
        echo $filename
        python /media/gcx/1t/gccruz_academiafa/workspace/labelling_utils/get_gt_stats.py $filename 1920 1080
  done
done
cd -