import numpy as np
import matplotlib.pyplot as plt


# Generate random samples for X and Y
np.random.seed(0)  # Set seed for reproducibility
num_samples = 10000
X = np.random.uniform(0, 1, num_samples)
Y = np.random.uniform(1, 2, num_samples)

# Calculate joint probability distribution
joint_distribution = np.histogram2d(X, Y, bins=[10, 10], range=[[0, 1], [1, 2]])[0] / num_samples
print(joint_distribution)
# Calculate marginal probabilities
marginal_X = np.sum(joint_distribution, axis=1)
marginal_Y = np.sum(joint_distribution, axis=0)

# Check independence
independence_check = np.allclose(joint_distribution, np.outer(marginal_X, marginal_Y))
if independence_check:
    print("X and Y are independent events.")
else:
    print("X and Y are not independent events.")
# Find indices corresponding to Y = 1.5
y_index = np.argmin(np.abs(np.linspace(1, 2, 10) - 1.5))

# Calculate conditional probability P(X > 0.5 | Y = 1.5)
conditional_prob = np.sum(joint_distribution[y_index:, :5]) / np.sum(joint_distribution[y_index:])
print("Conditional Probability of X > 0.5 given Y = 1.5:", conditional_prob)
# Plot conditional probability distribution
l=[]
for i in range(len(Y)):
    if Y[i]==1.5:
        l.append(i)
lM=[]
for j in l:
    lM.append(X[i])
plt.subplot(1,2,1)
plt.hist(lM)
plt.title('Conditional Probability Distribution of X | Y = 1.5')
plt.xlabel('X')
plt.ylabel('Conditional Probability')
plt.subplot(1,2,2)
plt.bar(np.linspace(0, 1, 10),1)
plt.xlim(0, 1)
plt.show()

