from scipy.stats import norm, uniform, truncexpon
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# PART A

# Random Number Generators
# i. Uniform distribution
uniform_samples = uniform.rvs(size=1000)
ax.hist(uniform_samples, bins=10, density=True, alpha=0.75, label='Uniform')

# ii. Normal distribution
normal_samples = norm.rvs(size=1000)
ax.hist(normal_samples, bins=30, density=True, alpha=0.75, label='Normal')

# iii. Truncated exponential distribution
truncexpon_samples = truncexpon.rvs(b=2, size=1000)
ax.hist(truncexpon_samples, bins=30, density=True, alpha=0.75, label='Truncated Exponential')

# Density Functions
# Uniform distribution
x = np.linspace(0, 1, 1000)
ax.plot(x, uniform.pdf(x), 'r-', lw=2)

# Normal distribution
x = np.linspace(-4, 4, 1000)
ax.plot(x, norm.pdf(x), 'g-', lw=2)

# Truncated exponential distribution
x = np.linspace(0, 6, 1000)
ax.plot(x, truncexpon.pdf(x, b=2), 'b-', lw=2)

ax.legend()
plt.show()

# PART B

# pdf func:
# f(x) = (2x+3)/40 : 0<x<5 
# range of f(x) = 0.075 to 0.325

# cdf func:
# F(x) = (x^2 + 3x)/40 : 0<x<5

# for rv generation: calculation of inv-cdf
# x = (-3 + sqrt(9 + 160y))/2

# PDF func:
def pdf(x):
    if x < 0: return 0
    elif x > 5: return 0
    else: return (2*x+3)/40

# Inverse CDF func:
def inv_cdf(y):
    return (-3 + np.sqrt(9 + 160*y))/2

# Random Number Generator
random_samples = inv_cdf(np.random.uniform(0, 1, size=10000))

# Plotting
fig, ax = plt.subplots()
x = np.linspace(-2, 7, 1000)
ax.plot(x, [pdf(i) for i in x], 'r-', label='PDF')
ax.hist(random_samples, bins=20, density=True, alpha=0.75, label='Random Samples')
ax.legend()
plt.show()