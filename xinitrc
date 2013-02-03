xset s off
xset -dpms
xset s noblank
xhost +

#
#DATA_DIR="/media/Pictures/Vivek-iPhone-4S"
DATA_DIR="/media/Pictures/Petra-Varney-2011"
#DATA_DIR="/media/Pictures"

feh --recursive -F -Z -Y -z --draw-tinted -D5 $DATA_DIR --info "rm -rf /data/current/*; cp %f /data/current; echo %f; exifgrep '(GPS|Gps.*)' %F | cut -d . -f 4-;"
