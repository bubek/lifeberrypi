#!/bin/sh

DIRECTORY=`dirname $0`
. ${DIRECTORY}/common.sh

killall feh
$HDMI -p
. /etc/rc.local
