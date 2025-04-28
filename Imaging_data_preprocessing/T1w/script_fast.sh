#!/bin/bash

# read inputs

list=$1

dos2unix $list

for filename in `cat $list`; do

fast -o fast_${filename}/${filename} flirt_${filename}

done
