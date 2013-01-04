#!/bin/sh

mkdir /media

mkdir /data
chown pi:pi /data
mkdir /data/current
chown pi:pi /data/current


git config --global user.name "Vivek Bhaskaran"
git config --global user.email vivek.bhaskaran@surveyanalytics.com


cp etc/rc.local /etc/
cp pi/.xinitrc ~pi/
chown pi:pi ~pi/.xinitrc
