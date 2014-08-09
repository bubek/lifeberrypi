#!/bin/sh


PACKAGES="git x11-xserver-utils exifprobe feh x11-apps emacs apache2 tcpdump portmapper"

apt-get update
apt-get -y install $PACKAGES
