#!/bin/bash
daylist=""
day800list=""
for i in `seq 1 4 240`;
do
    ni=`expr 1440 - ${i}`
    pni=`printf '%04d' ${ni}`
    daylist="frames/loop${pni}.gif $daylist"
    day800list="frames800/loop${pni}.gif $day800list"
done

convert  -delay 4  -loop 0 ${daylist} loop_4hours.gif
convert  -delay 4  -loop 0 ${day800list} loop800_4hours.gif

