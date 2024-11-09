import matplotlib.pyplot as plt
import numpy as np

X_axis = np.array([0, 1, 2, 3, 4, 5])
frequency = np.array([2, 11, 23, 9, 4, 1])

total_students = np.sum(frequency)

# Probability Mass Function (PMF)
PMF = frequency / total_students

# Cumulative Distribution Function (CDF)
CDF = np.cumsum(PMF)
print(CDF)
# Plotting PMF using a bar plot
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(X_axis, PMF, color="blue")
plt.title("Probability Mass Function (PMF)")
plt.xlabel("No. of times the lie detector buzzes")
plt.ylabel("Probability")
plt.xticks(X_axis)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.step(X_axis, CDF, where='post', color="green")
plt.title("Cumulative Distribution Function (CDF)")
plt.xlabel("No. of times the lie detector buzzes")
plt.ylabel("Cumulative Probability")
plt.xticks(X_axis)
plt.grid(True)

plt.tight_layout()
plt.show()


#theoretical mean and standard dev
result=X_axis * frequency
sum_result=np.sum(result)
theoretical_mean=sum_result/total_students
theoretical_std = np.sqrt(np.sum(((X_axis - theoretical_mean) ** 2) * PMF))
print("Theoretical mean:", theoretical_mean)
print("Theoretical standard deviation:", theoretical_std)


#For 50 trials
simulated_values = np.random.choice(X_axis, size=50, p=frequency / 50)
simulated_mean = np.mean(simulated_values)
simulated_std = np.std(simulated_values)
print("the mean for 50 trials is: ",simulated_mean)
print("the std_dev for 50 trials is: ",simulated_std)

#for 500 trials
simulated_values = np.random.choice(X_axis, size=500, p=frequency / 50)
simulated_mean = np.mean(simulated_values)
simulated_std = np.std(simulated_values)
print("the mean for 500 trials is: ",simulated_mean)
print("the std_dev for 500 trials is: ",simulated_std)

#for 5000 trials
simulated_values = np.random.choice(X_axis, size=5000, p=frequency / 50)
simulated_mean = np.mean(simulated_values)
simulated_std = np.std(simulated_values)
print("the mean for 5000 trials is: ",simulated_mean)
print("the std_dev for 5000 trials is: ",simulated_std)




# Choose a value for n (number of experiments)
n = 20  

# Repeat the experiment n times and calculate mean each time, repeat 1000 times
sample_means = []
for i in range(1000):
    simulated_values = np.random.choice(X_axis, size=n, p=frequency / total_students)
    sample_mean = np.mean(simulated_values)
    sample_means.append(sample_mean)

# Plot a histogram 
plt.hist(sample_means, bins=30, color="blue")
plt.title(f'Histogram of Sample Means (n={n})')
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Calculate mean and variance of sample means
sample_mean = np.array(sample_means)
mean_of_sample_mean = np.mean(sample_means)
variance_of_sample_mean = np.var(sample_means)
print("Mean :", mean_of_sample_mean)
print("Variance :", variance_of_sample_mean)


# The histogram of sample means tends to follow a normal distribution, especially as n increases, due to the Central Limit Theorem.
# The statement "The sample mean is a Random Variable" is true since the sample mean can vary from one sample to another,
# depending on the random selection of observations from the population.
