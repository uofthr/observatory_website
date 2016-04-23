import ephem
import datetime
import os

o=ephem.Observer()
o.lat='43.7845659'
o.long='-79.1906955'
sun=ephem.Sun()
sun.compute()
now = datetime.datetime.now()
rising = ephem.localtime(o.next_rising(sun))
setting =  ephem.localtime(o.previous_setting(sun))


ps =  (now-setting).seconds/60.
nr =  (rising-now).seconds/60.
print(ps)
print(nr)
if ps>91. and nr >91.:
    # night mode
    command = "raspistill -ss 30000000 -ISO 100 -w 960 -h 720 -o latest.jpg && scp latest.jpg rein@rein.utsc.utoronto.ca:~/public_html/observatory/webcam/ && ssh rein@rein.utsc.utoronto.ca 'cd /home/rein/public_html/observatory/webcam/ && bash update_frames.bash'"
else:
    #day mode
    command = "raspistill -w 960 -h 720 -o latest.jpg && scp latest.jpg rein@rein.utsc.utoronto.ca:~/public_html/observatory/webcam/ && ssh rein@rein.utsc.utoronto.ca 'cd /home/rein/public_html/observatory/webcam/ && bash update_frames.bash'"

os.system(command)
