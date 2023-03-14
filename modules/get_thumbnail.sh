#!/bin/bash/

wget $1

filename=$(basename $1)
fname=$2

ext=$3

mv "$filename" "$fname.$ext"
