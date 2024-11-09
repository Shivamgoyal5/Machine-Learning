import numpy as np
import matplotlib.pyplot as plt
import random

overall_frequency = []

# Initialize the overall_frequency list with zeros
for i in range(2, 13):
    overall_frequency.append(0)

# Simulate 10,000 dice rolls
for i in range(10000):
    face1 = random.randint(1, 6)
    face2 = random.randint(1, 6)
    dice_output = face1 + face2
    overall_frequency[dice_output - 2] += 1

# Plot the probability distribution
plt.bar(range(2, 13,1), overall_frequency, color="blue")
plt.title("Probability Distribution of Two Dice Sum")
plt.xlabel("Sum of Two Dice")
plt.ylabel("Probability of each outcome")
plt.xticks(range(2, 13, 1))
plt.savefig("sumofdices")
plt.show()
