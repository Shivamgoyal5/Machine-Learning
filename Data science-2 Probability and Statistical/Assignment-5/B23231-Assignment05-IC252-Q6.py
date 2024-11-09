# f(x) = \int_-^{pi} \sin^{4} (3x) dx
# Clearly max value of sin^4 (3x) is 1
# Range of Integral is [0, pi] -> rect of len pi and height 1

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# define function to be integrated:
f = lambda x: np.sin(3*x)**4

# Plot the function:
fig, ax = plt.subplots(ncols=2, figsize=(10, 5))
x = np.linspace(0, np.pi, 100)
y = f(x)
ax[0].plot(x, y)

# Calculate the actual value of integral:
actual_integral = quad(f, 0, np.pi)[0]
ax[1].axhline(y=actual_integral, color='red', linestyle='-')

# Number of points to be generated:
N = 2000

# MONTE CARLO INTEGRATION:  
count = 0
for i in range(N):
    x = np.random.rand()*np.pi
    y = np.random.rand()
    if y < f(x):
        count += 1

    ax[0].plot(x, y, 'ro', markersize=2)
    ax[1].plot(i, np.pi*count/(i+1), 'ro', markersize=2)
    plt.pause(0.01)

plt.show()
    

# Calculate the integral:
integral = np.pi*count/N

print(f'Integral value from Simulation: {integral:.4f}')
print(f'Actual Integral Value: {actual_integral:.4f}')
