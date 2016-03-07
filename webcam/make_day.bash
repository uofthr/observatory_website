#!/bin/bash
daylist=""
for i in `seq 1 24 1440`;
do
    ni=`expr 1440 - ${i}`
    pni=`printf '%04d' ${ni}`
    daylist="frames/loop${pni}.gif $daylist"
done

convert  -delay 4  -loop 0 ${daylist} loop_day.gif
