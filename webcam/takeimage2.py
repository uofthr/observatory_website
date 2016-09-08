import ephem
import datetime
import os
import os.path

o=ephem.Observer()
o.lat='43.7845659'
o.long='-79.1906955'
sun=ephem.Sun()
sun.compute()
now = datetime.datetime.now()
rising = ephem.localtime(o.next_rising(sun))
setting =  ephem.localtime(o.previous_setting(sun))
nsetting =  ephem.localtime(o.next_setting(sun))


ps =  (now-setting).seconds/60.
nr =  (rising-now).seconds/60.
print(ps)
print(nr)
if ps>91. and nr >91. and rising<nsetting:
    if nr > 91.+30:
        if not os.path.isfile("running.tag"):
            with open("running.tag", "w+") as f: 
                f.write("running now")
            vidc = "raspivid -awb sun -ex night -pf high -ISO 800 -g 1 -qp 10 -ss 6000000 -t 1200000 -b 100000000 -o out.h264"  
            command = vidc + " && scp out.h264 rein@rein.utsc.utoronto.ca:~/public_html/observatory/webcam/ && ssh rein@rein.utsc.utoronto.ca 'cd /home/rein/public_html/observatory/webcam/ && bash update_nightvideo.bash'"
            os.system(command)
            os.remove("running.tag")
else:
    #day mode
    command = "raspistill -w 960 -h 720 -o latest.jpg && scp latest.jpg rein@rein.utsc.utoronto.ca:~/public_html/observatory/webcam/ && ssh rein@rein.utsc.utoronto.ca 'cd /home/rein/public_html/observatory/webcam/ && bash update_frames.bash'"
    os.system(command)

#print command
