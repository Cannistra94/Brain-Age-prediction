#!/bin/bash

## bedpostx

# read inputs
subject_id=$1

bedpostx ${subject_id} --nf=2 --fudge=1 --bi=1000
