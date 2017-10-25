#!/usr/bin/python
import numpy
import datetime as dt
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.dates as md

fig, ax = plt.subplots(1,1,figsize=(6,3))
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.set_ylabel("sky brightness [mpas]")

with open('skyquality.log', 'r') as content_file:
    log = content_file.readlines()

time = []
ms = []
for r in log:
    c = r.split(",")
    t = int(c[0])
    m = float(c[2][:-1])
    time.append(dt.datetime.fromtimestamp(t))
    ms.append(m)

ax.plot(time,ms)
fig.savefig("skyquality.png")
