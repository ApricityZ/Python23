from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_axes( Axes3D(fig))

x = np.arange(-100,100, 1)
y = np.arange(-100,100, 1)

X, Y = np.meshgrid(x, y)
Z = 5 * X ** 2 + 8 * X * Y + 5 * Y ** 2

plt.xlabel('x')
plt.ylabel('y')

ax.plot_surface(X, Y, Z,rstride=1,cstride=1,cmap='rainbow')
plt.show()
