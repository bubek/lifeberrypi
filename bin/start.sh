#!/bin/sh

DIRECTORY=`dirname $0`
. ${DIRECTORY}/common.sh

$HDMI -p
killall feh



