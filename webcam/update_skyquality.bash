#!/bin/bash
sleep 4
ISNIGHT="isnight45.tag"
if [ -f $ISNIGHT ]; then
    MESSAGES=( "Current sky brigthness at the @UTSCObservatory:" )
    i=$(( RANDOM % ${#MESSAGES[@]} ))
    VALUE=`awk -F, "{print \\$2}" data.txt`
    echo $VALUE
    MESSAGE="${MESSAGES[i]}${VALUE}psas (magnitudes per square arcsecond). 🔭🌃"
    python update_skyquality_plot.py
    ./uploadToTwitter.bash "$MESSAGE" skyquality.png nocheck
fi
