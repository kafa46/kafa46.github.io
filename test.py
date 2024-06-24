import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

artists = []
for i in range(len(x)):
    point, = ax.plot(x[i], y[i], 'ro')
    artists.append([point])

ani = animation.ArtistAnimation(fig, artists, interval=50, blit=True)
plt.show()
