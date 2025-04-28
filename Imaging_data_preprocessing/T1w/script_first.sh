#!/bin/bash

# read inputs

list=$1

dos2unix $list

for filename in `cat $list`; do

run_first_all -i ${filename}.nii -o first_${filename}.nii -b


done
