#!/bin/bash/

wget $1

filename=$(basename $1)
fname=$2

ext=$3

mkdir -p $4

mv "$filename" "$fname.$ext"
mv "$fname.$ext" $4
