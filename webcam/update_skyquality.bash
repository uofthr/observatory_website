#!/bin/bash


MESSAGES=( "Current sky brightness at the @UTSCObservatory:" )
i=$(( RANDOM % ${#MESSAGES[@]} ))
VALUE=`awk -F, "{print \\$2}" data.txt`
echo $VALUE
MESSAGE="${MESSAGES[i]} ${VALUE}psas (magnitudes per square arcsecond). 🔭🌃"

#DATE=`date +"%B %d %Y, %H:%M"`
/usr/local/bin/twurl "/1.1/statuses/update.json" -d "status=$MESSAGE"
