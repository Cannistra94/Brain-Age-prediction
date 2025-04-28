#!/bin/bash

# read inputs

list=$1

dos2unix $list

for filename in `cat $list`; do

echo ${filename},`fslstats -K left_temporal_pole.nii.gz ${filename}_pve_1.nii.gz -V | awk '{print $2}'` >> left_temporal_pole.csv

done
