#!/bin/bash

# read inputs

list=$1

dos2unix $list

for filename in `cat $list`; do

bet bet_${filename}.nii ${filename}.nii 

done
