# Initial Position : 0
# 1D walk with setpsize : 1 or -1 with equal probability
import numpy as np
import matplotlib.pyplot as plt

repeat_expt = 100000
steps = 1000  # total number of steps

positions = []

# PART A
for _ in range(repeat_expt):
    positions.append(sum(np.random.choice([-1, 1], steps)))

# PART B
# for _ in range(repeat_expt):
#     positions.append(sum(np.random.choice([-1, 1], steps, p=[0.4, 0.6])))


plt.hist(positions, bins=80, density=True)
plt.xlabel('Position')
plt.ylabel('Probability')
plt.show()