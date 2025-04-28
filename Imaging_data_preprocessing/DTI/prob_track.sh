#!/bin/bash

# read inputs

filename=$1


/usr/pubsw/packages/fsl/6.0.3/bin/probtrackx2  -x seed.nii.gz  -l --onewaycondition -c 0.2 -S 2000 --steplength=0.5 -P 5000 --fibthresh=0.01 --distthresh=0.0 --sampvox=0.0 --xfm=${filename}.bedpostX/xfms/standard2diff.mat --avoid=exclude.nii.gz --forcedir --opd -s ${filename}.bedpostX/merged -m ${filename}.bedpostX/nodif_brain_mask  --dir=${filename} --targetmasks=${filename}/targets.txt --os2t
