#!/bin/bash

# read inputs

list=$1

dos2unix $list

for filename in `cat $list`; do

dcm2niix -o ${filename} -z y -v y ${filename}/DTI/009

done
