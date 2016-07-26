import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
if os.path.isfile("isnight.tag"):
    latest = plt.imread("latestnight.jpg")
    try:
        longtime_sum = np.load("longtime_sum.npy")
        longtime_sum += latest.astype(long)
    except:
        longtime_sum = latest.astype(long)
    np.save("longtime_sum",longtime_sum)

    try:
        longtime_max = np.load("longtime_max.npy")
        longtime_max = np.maximum(longtime_max,latest.astype(long))
    except:
        longtime_max = latest.astype(long)
    np.save("longtime_max",longtime_max)

    doubletime_sum = longtime_sum.astype(np.float64)
    mi = np.min(doubletime_sum)
    ma = np.max(doubletime_sum)
    doubletime_sum = 255.*np.sqrt((doubletime_sum-mi)/(ma-mi))
    doubletime_sum = np.clip(doubletime_sum,0,255)
    inttime_sum = doubletime_sum.astype(np.uint8)
    matplotlib.image.imsave("longtimeexposure.png",inttime_sum)

    doubletime_sum = longtime_max.astype(np.float64)
    mi = np.min(doubletime_sum)
    ma = np.max(doubletime_sum)
    doubletime_sum = 255.*np.sqrt((doubletime_sum-mi)/(ma-mi))
    doubletime_sum = np.clip(doubletime_sum,0,255)
    inttime_sum = doubletime_sum.astype(np.uint8)
    matplotlib.image.imsave("longtimeexposure_max.png",inttime_sum)
