#!/usr/bin/python
import numpy as np
import datetime as dt
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.dates as md

fig, ax = plt.subplots(1,1,figsize=(6,3))
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.set_ylabel("sky brigthness [mag/arcsec${}^2$]")
ax.invert_yaxis()
ax.set_title('UTSC Observatory/RASCTC', loc='right')



with open('skyquality.log', 'r') as content_file:
    log = content_file.readlines()

time = []
ms = []
for r in log:
    c = r.split(",")
    try:
        t = int(c[0])
        m = float(c[2][:-1])
        time.append(dt.datetime.fromtimestamp(t))
        ms.append(m)
    except:
        pass

ax.plot(time,ms)
lowlim=20
ax.set_ylim([lowlim,7.5])
ax.set_xlim([time[0],time[-1]])
low = lowlim*np.ones(len(time))
ax.fill_between(time,ms,low, alpha=0.5)
fig.savefig("skyquality.png",bbox_inches='tight')
