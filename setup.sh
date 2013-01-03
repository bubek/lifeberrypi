#!/bin/sh

mkdir /media
mkdir /data
mkdir /data/current


git config --global user.name "Vivek Bhaskaran"
git config --global user.email vivek.bhaskaran@surveyanalytics.com


cp rc.local /etc/
cp .xinitrc ~pi/
chown pi:pi ~pi/.xinitrc
