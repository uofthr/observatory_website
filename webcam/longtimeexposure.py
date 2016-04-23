import numpy as np
import matplotlib.pyplot as plt
import matplotlib
latest = plt.imread("latest.jpg")
try:
    longtime_sum = np.load("longtime_sum.npy")
    longtime_sum += latest.astype(long)
except:
    longtime_sum = latest.astype(long)
np.save("longtime_sum",longtime_sum)

doubletime_sum = longtime_sum.astype(np.float64)
med = np.median(doubletime_sum)
doubletime_sum *= 32./med

inttime_sum = doubletime_sum.astype(np.uint8)
clipped = np.clip(inttime_sum,0,255)
matplotlib.image.imsave("longtimeexposure.png",clipped)
