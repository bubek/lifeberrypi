#!/bin/sh


PACKAGES="git x11-xserver-utils exifprobe feh x11-apps emacs"

apt-get update
apt-get -y install $PACKAGES
