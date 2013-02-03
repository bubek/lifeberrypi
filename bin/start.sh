#!/bin/sh

DIRECTORY=`dirname $0`
. ${DIRECTORY}/common.sh

$HDMI -p

killall feh
kill `pidof X`

su -c startx pi &
sleep 2
killall feh
su -c startx pi &
