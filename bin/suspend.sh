#!/bin/sh

DIRECTORY=`dirname $0`
. ${DIRECTORY}/common.sh

# suspend the slideshow
$XDOTOOL key h
$HDMI -o
killall feh


