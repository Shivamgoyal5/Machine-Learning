import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# user input for lambda:
lmbda = float(input("Enter the value of lambda: "))
n = 100

samples = []

for i in range(5):
    sample = expon.rvs(scale=1/lmbda, size=n)
    samples.append(sample)

# Plotting the samples - any 3:
plt.figure(figsize=(10, 5))
plt.title('Exponential Distribution with lambda = '+str(lmbda)+' and n = '+str(n))
indices = np.random.choice(5, 3, replace=False)

for i in indices:
    plt.hist(samples[i], bins=20, alpha=0.4, label='Sample '+str(i+1), density=True)

# Plotting the exponential distribution
x = np.linspace(0, 10, 1000)
plt.plot(x, expon.pdf(x, scale=1/lmbda), 'r', label='Exponential Distribution')


# Comparing the samples with the actual exponential distribution
means = [round(np.mean(sample), 3) for sample in samples]
variances = [round(np.var(sample), 3) for sample in samples]
std_devs = [round(np.sqrt(var), 3) for var in variances]

print('Sample Means:', means)
print('Sample Variances:', variances)
print('Sample Standard Deviations:', std_devs)

# Actual mean and variance of the exponential distribution
actual_mean = 1/lmbda
actual_variance = 1/lmbda**2
actual_std_dev = 1/lmbda

print('Actual Mean:', actual_mean)
print('Actual Variance:', actual_variance)
print('Actual Standard Deviation:', actual_std_dev)

plt.legend()
plt.show()
