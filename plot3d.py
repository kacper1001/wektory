
# Is = 4 + 2 * np.cos(2 * k * sinteta * X) + 2 * np.cos(2 * k * sinteta * Y)
#
# Ip = 4 + 2 * np.cos(2 * k * sinteta * X) + 2 * np.cos(2 * k * sinteta * Y) \
#      + 4 * np.cos(k * sinteta * X) * np.cos(k * sinteta * Y)
#
# Is = 4 - 2 * np.cos(2 * k * sinteta * X) - 2 * np.cos(2 * k * sinteta * Y)
#
# Ips = 4 - 2 * np.cos(2 * k * sinteta * X) \
#       - 4 * costeta * np.cos(k * sinteta * (X + Y)) \
#       + 4 * costeta * np.cos(k * sinteta * (X - Y)) \
#       + 2 * np.cos(2 * k * sinteta * Y) * (sinteta * sinteta - costeta * costeta)
#
# Ip = 4 \
#      + 2 * np.cos(2 * k * sinteta * X) * (sinteta * sinteta - costeta * costeta) \
#      + 2 * np.cos(2 * k * sinteta * Y) * (sinteta * sinteta - costeta * costeta) \
#      - 8 * costeta * np.cos(k * sinteta * (X + Y)) \
#      + 4 * costeta * np.cos(k * sinteta * (X - Y)) \
#      + 4 * costeta * np.cos(k * sinteta * (-X + Y))


import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


figIs = plt.figure()
ax = figIs.gca(projection='3d')

k = (np.pi * 2 / 0.532)
theta = 4 * np.pi / 180
sinteta = np.sin(theta)
costeta = np.cos(theta)

x = np.arange(-8, 8, 0.1)
y = x
X, Y = np.meshgrid(x, y)

Is = 4 + 2 * np.cos(2 * k * sinteta * X) + 2 * np.cos(2 * k * sinteta * Y)

surfs = ax.plot_surface(X, Y, Is, cmap=cm.hot, linewidth=0, antialiased=False)

ax.set_zlim(0, 17)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

figIs.colorbar(surfs, shrink=0.5, aspect=5)

plt.show()



figIp = plt.figure()
ax = figIp.gca(projection='3d')

k = (np.pi * 2 / 0.532)
theta = 4 * np.pi / 180
sinteta = np.sin(theta)
costeta = np.cos(theta)

x = np.arange(-8, 8, 0.1)
y = x
X, Y = np.meshgrid(x, y)

Ip = 4 - 2 * np.cos(2 * k * sinteta * X) - 2 * np.cos(2 * k * sinteta * Y) \
      + 4 * sinteta * np.cos(k * sinteta * X) * np.cos(k * sinteta * Y)

surfs = ax.plot_surface(X, Y, Ip, cmap=cm.hot, linewidth=0, antialiased=False)

ax.set_zlim(0, 17)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

figIp.colorbar(surfs, shrink=0.5, aspect=5)

plt.show()
