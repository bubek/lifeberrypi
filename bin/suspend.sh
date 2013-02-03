#!/bin/sh

DIRECTORY=`dirname $0`
. ${DIRECTORY}/common.sh

$HDMI -o
killall feh
kill `pidof X` 
