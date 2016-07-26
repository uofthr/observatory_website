#!/bin/bash

./make_hour.bash


LID=`cat lid.txt`
LID=$((LID+1))
echo $LID >  lid.txt
LIDP=`printf '%09d' ${LID}`
cp latest.jpg frames_id/frame_${LIDP}.jpg

find frames_id/* -mtime +3 -exec rm {} \;
