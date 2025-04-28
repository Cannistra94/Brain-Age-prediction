#!/bin/bash

# read inputs

list=$1

dos2unix $list

for filename in `cat $list`; do

fslroi ${filename}/dti ${filename}/nodif 0 1

bet ${filename}/nodif ${filename}/nodif_brain -m -f 0.2

eddy_openmp --imain=${filename}/dti --mask=${filename}/nodif_brain_mask --acqp=acqparams.txt --index=index.txt --bvecs=${filename}/bvecs --bvals=${filename}/bvals --repol --out=${filename}/eddy_corr

dtifit -k ${filename}/eddy_corr -m ${filename}/nodif_brain_mask -r ${filename}/bvecs -b ${filename}/bvals -o ${filename}/data

done
