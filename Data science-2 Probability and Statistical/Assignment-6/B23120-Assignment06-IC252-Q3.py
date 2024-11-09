import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# user input for mean and std deviation:
mean = float(input("Enter mean: "))
std_dev = float(input("Enter stardard deviation: "))
n = 100

samples = []

for i in range(5):
    sample = norm.rvs(loc=mean, scale=std_dev, size=n)
    samples.append(sample)

# Plotting the samples - any 3:
plt.figure(figsize=(10, 5))
plt.title('Normal Distribution with n = '+str(n))
indices = np.random.choice(5, 3, replace=False)

for i in indices:
    plt.hist(samples[i], bins=20, alpha=0.4, label='Sample '+str(i+1), density=True)

# Plotting the exponential distribution
x = np.linspace(-10, 10, 1000)
plt.plot(x, norm.pdf(x, scale=std_dev, loc=mean), 'r', label='Exponential Distribution')


# Comparing the samples with the actual exponential distribution
means = [round(np.mean(sample), 3) for sample in samples]
variances = [round(np.var(sample), 3) for sample in samples]
std_devs = [round(np.sqrt(var), 3) for var in variances]

print('Sample Means:', means)
print('Sample Variances:', variances)
print('Sample Standard Deviations:', std_devs)

# Actual mean and variance of the exponential distribution
actual_mean = mean
actual_variance = std_dev**2
actual_std_dev = std_dev

print('Actual Mean:', actual_mean)
print('Actual Variance:', actual_variance)
print('Actual Standard Deviation:', actual_std_dev)

plt.legend()
plt.show()
