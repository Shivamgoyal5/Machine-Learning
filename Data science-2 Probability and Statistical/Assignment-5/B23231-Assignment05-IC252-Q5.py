import matplotlib.pyplot as plt
import numpy as np

POINTS = 1000
_y = []
current_pi = 0
fig, ax = plt.subplots(ncols=2, figsize=(10, 5))
ax[0].add_patch(plt.Circle((0, 0), 1, color='black', fill=False))
ax[1].set_title(f"Evolution of pi estimation")
ax[1].axhline(y=np.pi, color='red', linestyle='--')

for _ in range(POINTS):
    x, y = np.random.rand(2)*2-1
    if x**2 + y**2 <= 1:
        current_pi += 1
    _y += [current_pi*4/(_+1)]

    ax[0].plot(x, y, 'ro', markersize=3)
    ax[0].set_title(f"Current value of pi: {current_pi*4/(_+1):.4f}")

    ax[1].plot(_+1, current_pi*4/(_+1), 'ro', markersize=2)
    plt.pause(0.005)

plt.show()