#!/bin/bash
hourlist=""
for i in `seq 1 1 60`;
do
    ni=`expr 1440 - ${i}`
    pni=`printf '%04d' ${ni}`
    hourlist="frames/loop${pni}.gif $hourlist"
done

convert  -delay 4  -loop 0 ${hourlist} loop_hour.gif
