#!/bin/bash

# read inputs

list=$1

dos2unix $list

for filename in `cat $list`; do

/usr/pubsw/packages/fsl/6.0.3/bin/flirt -in ${filename}.bedpostX/nodif_brain -ref MNI152_T1_1mm.nii.gz -omat ${filename}.bedpostX/xfms/diff2standard.mat -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12

/usr/pubsw/packages/fsl/6.0.3/bin/convert_xfm -omat ${filename}.bedpostX/xfms/standard2diff.mat -inverse ${filename}.bedpostX/xfms/diff2standard.mat

done
