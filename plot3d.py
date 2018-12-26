# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

k = (np.pi * 2 / 0.532)
theta = 4 * np.pi / 180
sinteta = np.sin(theta)
costeta = np.cos(theta)

x = np.arange(-7.5, 7.5, 0.1)
y = x
X, Y = np.meshgrid(x, y)

Is = 4 - 2 * np.cos(2 * k * sinteta * X) - 2 * np.cos(2 * k * sinteta * Y)

Ips = 4 - 2 * np.cos(2 * k * sinteta * X)\
     - 4 * costeta * np.cos(k * sinteta * (X + Y)) \
     + 4 * costeta * np.cos(k * sinteta * (X - Y)) \
     + 2 * np.cos(2 * k * sinteta * Y) * (sinteta *sinteta - costeta*costeta)

Ip = 4 \
     + 2 * np.cos(2 * k * sinteta * X) * (sinteta * sinteta - costeta*costeta)\
     - 4 * costeta * np.cos(k * sinteta * (X + Y)) \
     - 4 * costeta * np.cos(k * sinteta * (-X + Y)) \
     + 4 * costeta * np.cos(k * sinteta * (X - Y)) \
     + 4 * costeta * np.cos(k * sinteta * (-X - Y)) \
     + 2 * np.cos(2 * k * sinteta * Y) * (sinteta * sinteta - costeta*costeta)

surfs = ax.plot_surface(X, Y, Ip, cmap=cm.hot, linewidth=0, antialiased=False)

ax.set_zlim(0, 13)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surfs, shrink=0.5, aspect=5)


plt.show()
