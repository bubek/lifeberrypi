#!/bin/sh

if [ -z "$1" ]
  then
    echo "No arguments supplied : Usage : process_image.sh"
    exit
fi

echo "Processing Image [$1]"
echo "var currentImage = {filename : $1}" > /data/current/filename.js
