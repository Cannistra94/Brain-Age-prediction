#!/bin/bash

# read inputs

list=$1

dos2unix $list

for filename in `cat $list`; do

robustfov -i /${filename}/anat.nii.gz -r /${filename}/anat.nii.gz 

done
