import matplotlib
import matplotlib.pyplot as plt
import numpy as np

resolution = ['720x1280 - 100%', '648x1152 - 90%', '576x1024 - 80%', '504x896 - 70%', '432x768 - 60%', '360x640 - 50%', '288x512 - 40%', '216x384 - 30%', '144x256 - 20%', '72x128 - 10%']
fps = [5.236845621, 7.190630487, 8.692707652, 13.29773868, 17.55813708, 21.47213962, 33.04742942, 51.67195856, 79.95476721, 128.2415449]

fig, ax = plt.subplots()
ax.plot(resolution, fps)

ax.set(xlabel='Resolution', ylabel='FPS',
       title='Image Resolution vs. FPS')
ax.grid()
plt.tight_layout()
plt.xticks(rotation=90)
plt.tight_layout()
fig.savefig("test.png")
#plt.show()