# -*- coding: utf-8 -*-
import ephem
import datetime
import os

o=ephem.Observer()
o.lat='3.7845659'
o.long='-79.1906955'
o.pressure = 0
o.horizon = '-1.5' 
sun=ephem.Sun()
sun.compute()
now = datetime.datetime.now()
rising = ephem.localtime(o.next_rising(sun))
setting =  ephem.localtime(o.next_setting(sun))
drn = (rising - now).seconds
if drn>0 and drn<60 :
    os.system("bash uploadToTwitter.bash 'Good morning! Sunrise in #ScarbTO happening right now! Live view from the #UTSC observatory 🌄'")

dsn = (setting - now).seconds
if dsn>0 and dsn<60:
    os.system("bash uploadToTwitter.bash 'Sunset in #Toronto! Live view from the #UTSC observatory 🌇'")

if drn>dsn:
    # Day light
    if now.minute==0:
        # Full hour
        os.system("bash uploadToTwitter.bash")

setting =  ephem.localtime(o.previous_setting(sun))
rising =  ephem.localtime(o.previous_rising(sun))
pns = ((now-setting).seconds)
min90 = 5400 #7320 # 5400
duration = (setting-rising).seconds/60
start = 1439 - duration - 90 - 90
if (pns>min90 and pns < min90+60) or 0:
    # Sun set 90 minutes ago
    os.system("bash uploadVideoToTwitter.bash %d 'Sunset occured 90 minutes ago in #Scarborough! Here is the entire day as a #timelapse from 🌄 to 🌇.'" % start)
