#!/bin/bash
#hourlist=""
#hour800list=""
#for i in `seq 1 1 60`;
#do
#    ni=`expr 1440 - ${i}`
#    pni=`printf '%04d' ${ni}`
#    hourlist="frames/loop${pni}.gif $hourlist"
#    hour800list="frames800/loop${pni}.gif $hour800list"
#done
#
#convert  -delay 4  -loop 0 ${hourlist} loop_hour.gif
#convert  -delay 4  -loop 0 ${hour800list} loop800_hour.gif

LID=`cat lid.txt`
LIDHOUR=$((LID-60))
avconv -r 20 -start_number $LIDHOUR -i frames_id/frame_%09d.jpg -c:v libx264 -y last_hour.mp4
