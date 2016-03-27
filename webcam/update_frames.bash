#!/bin/bash
for i in `seq 1 1439`;
do
    pi=`printf '%04d' ${i}`
    ni=`expr ${i} - 1`
    pni=`printf '%04d' ${ni}`
    mv frames/loop${pi}.gif frames/loop${pni}.gif
    mv frames800/loop${pi}.gif frames800/loop${pni}.gif
done
convert latest.jpg -resize 800x600 frames800/loop1439.gif
convert latest.jpg -resize 400x300 frames/loop1439.gif

./make_hour.bash


LID=`cat lid.txt`
LID=$((LID+1))
echo $LID >  lid.txt
LIDP=`printf '%09d' ${LID}`
cp latest.jpg frames_id/frame_${LIDP}.jpg

LIDDAY=$((LID-1440))
LIDDAYP=`printf '%09d' ${LIDDAY}`
rm frames_id/frames_${LIDDAYP}.jpg
