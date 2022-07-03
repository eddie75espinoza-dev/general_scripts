#
# importing libraries
from random import triangular
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# defining surface and axes
x = np.outer(np.linspace(-1.5, 1.5, 10), np.ones(10))
y = x.copy().T
z = np.cos(x ** 3 + y ** 3)
fig = plt.figure()

# syntax for 3-D plotting
ax = plt.axes(projection='3d')

# syntax for plotting
# plot 2D or 3D data
#ax.plot(4, 4, 4)
# Plot a 3D wireframe
#ax.plot_wireframe(x, y, z, cmap = 'viridis', edgecolor = 'orangered')
# create a surface plot
ax.plot_surface(x, y, z, cmap = 'viridis', edgecolor = 'green')
ax.set_title('Surface plot python.hub')
plt.show()