import matplotlib.pyplot as plt
import numpy as np

# Data about cases
average_cases_per_hour = 57

# Calculating lambda for exponential distribution
lambda1 = 1 / average_cases_per_hour

# Define range of wait times (hours)
waiting_time = np.linspace(0, 500)  # Adjust the range as needed

# Calculate probability density function (PDF) using exponential distribution formula
pdf = lambda1 * np.exp(-lambda1 * waiting_time)

# Calculate cumulative distribution function (CDF) using exponential distribution formula
cdf = 1 - np.exp(-lambda1 * waiting_time)

# Plotting the PDF and CDF
plt.figure(figsize=(12, 6))

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(waiting_time, pdf, label="Exponential Distribution PDF", color="blue")
plt.title("Probability Density Function (PDF) for Waiting Time")
plt.xlabel("Wait Time (hours)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(waiting_time, cdf, label="Exponential Distribution CDF", color="green")
plt.title("Cumulative Distribution Function (CDF) for Waiting Time")
plt.xlabel("Wait Time (hours)")
plt.ylabel("Cumulative Probability")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

#(2) to find that the time for next +ve case is less than or equal to 1 minute i.e. 1/60 == 0.01677
proba_less_than_1_min= 1 - np.exp(-lambda1 * (1/60))
print("proba_less_than_1_min is:",proba_less_than_1_min)

#(3) to find between 1 min and 2 min
probab_between_1min_and_2min=np.exp(-lambda1 * (1/60))-np.exp(-lambda1 * (2/60))
print("probab_between_1min_and_2min is:",probab_between_1min_and_2min)

#(4)probab more than 2 min
probab_more_than_2min=1 - np.exp(-lambda1 * (2/60))
print("probab_more_than_2min is:",probab_more_than_2min)

#(5)probab between 1 and 2 min with double rate

new_avg_cases_per_hour = 2*(average_cases_per_hour)
new_lamda = 1/new_avg_cases_per_hour
new_probability_between_1_minute_and_2_minute=np.exp(-new_lamda * (1/60))-np.exp(-new_lamda * (2/60))