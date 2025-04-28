#!/bin/bash

# read inputs

list=$1

dos2unix $list

for filename in `cat $list`; do

/usr/pubsw/packages/fsl/6.0.3/bin/flirt -in ${filename}/data_FA.nii.gz -ref /autofs/cluster/pubsw/2/pubsw/Linux2-2.3-x86_64/packages/fsl.64bit/6.0.3/data/standard/FSL_HCP1065_FA_1mm.nii.gz -out ${filename}/FA_reg.nii.gz -omat ${filename}/FA_reg.mat -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12  -interp trilinear

/usr/pubsw/packages/fsl/6.0.3/bin/flirt -in ${filename}/data_L1.nii.gz -ref /autofs/cluster/pubsw/2/pubsw/Linux2-2.3-x86_64/packages/fsl.64bit/6.0.3/data/standard/FSL_HCP1065_L1_1mm.nii.gz -out ${filename}/L1_reg.nii.gz -omat ${filename}/L1_reg.mat -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12  -interp trilinear

/usr/pubsw/packages/fsl/6.0.3/bin/flirt -in ${filename}/data_L2.nii.gz -ref /autofs/cluster/pubsw/2/pubsw/Linux2-2.3-x86_64/packages/fsl.64bit/6.0.3/data/standard/FSL_HCP1065_L2_1mm.nii.gz -out ${filename}/L2_reg.nii.gz -omat ${filename}/L2_reg.mat -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12  -interp trilinear

/usr/pubsw/packages/fsl/6.0.3/bin/flirt -in ${filename}/data_L3.nii.gz -ref /autofs/cluster/pubsw/2/pubsw/Linux2-2.3-x86_64/packages/fsl.64bit/6.0.3/data/standard/FSL_HCP1065_L3_1mm.nii.gz -out ${filename}/L3_reg.nii.gz -omat ${filename}/L3_reg.mat -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12  -interp trilinear

/usr/pubsw/packages/fsl/6.0.3/bin/flirt -in ${filename}/data_MO.nii.gz -ref /autofs/cluster/pubsw/2/pubsw/Linux2-2.3-x86_64/packages/fsl.64bit/6.0.3/data/standard/FSL_HCP1065_MO_1mm.nii.gz -out ${filename}/MO_reg.nii.gz -omat ${filename}/MO_reg.mat -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12  -interp trilinear

/usr/pubsw/packages/fsl/6.0.3/bin/flirt -in ${filename}/data_MD.nii.gz -ref /autofs/cluster/pubsw/2/pubsw/Linux2-2.3-x86_64/packages/fsl.64bit/6.0.3/data/standard/FSL_HCP1065_MD_1mm.nii.gz -out ${filename}/MD_reg.nii.gz -omat ${filename}/MD_reg.mat -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12  -interp trilinear

done
