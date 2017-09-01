import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0, 1.0, 0.01)

fig = plt.figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(x, np.sin(2*2*np.pi*x))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_title("Sinuskurven")

for label in ax1.get_xticklabels():
    label.set_color('r')


ax2 = fig.add_subplot(212)
ax2.plot(x, np.sin(2*2*np.pi*x))
ax2.grid(True)
ax2.set_ylim((-2, 2))

l = ax2.set_xlabel("Strecke")
l.set_fontsize('large')

plt.show()
