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
    os.system("bash uploadToTwitter.bash 'Sunrise in Scarborough! Live view from the #UTSC observatory 🌄'")

dsn = (setting - now).seconds
if dsn>0 and dsn<60:
    os.system("bash uploadToTwitter.bash 'Sunset in Scarborough! Live view from the #UTSC observatory 🌇'")

if drn>dsn:
    # Day light
    if now.minute==0:
        # Full hour
        os.system("bash uploadToTwitter.bash")
