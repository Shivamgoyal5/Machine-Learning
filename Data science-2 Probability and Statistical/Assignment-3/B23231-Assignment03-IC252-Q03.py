import numpy as np
from statistics import NormalDist

# Constants
mean_weights = 150  # Mean weight of widgets
std_deviation = 10       # Standard deviation of widget weights
sample_size = 100  # Number of samples

# Simulate widget weights
widget_weights = np.random.normal(mean_weights, std_deviation, sample_size)


#first checking values less than 140 and automatically calculating their means
count_less_than_140_experimental = np.mean(widget_weights < 140)
count_less_than_140_theoretical=NormalDist(mean_weights, std_deviation).cdf(140)


#by using this key we are checking item at 95 percentile 
premium_experimental=np.percentile(widget_weights,95)
premium_theoretical=NormalDist(mean_weights, std_deviation).inv_cdf(1 - 0.05)

#by using this key we are checking item at 10 precentile
defective_experimental=np.percentile(widget_weights,10)
defective_theoretical=NormalDist(mean_weights, std_deviation).inv_cdf(0.1)

#probability of a product neither premium nor defective
nei_premium_nor_defective__experimental=1-((np.mean(widget_weights>=premium_experimental))+np.mean((widget_weights<=defective_experimental)))
nei_premium_nor_defective__theoretical=NormalDist(mean_weights, std_deviation).cdf(premium_experimental) - NormalDist(mean_weights, std_deviation).cdf(defective_experimental)


# Results
print("(1)experimental Probability of a widget weighs less than 140 grams:", count_less_than_140_experimental)
print("   theoretical Probability:", count_less_than_140_theoretical)
print("(2) experimental min weight for a premium product:", premium_experimental)
print("    theoretical min weight:", premium_theoretical)
print("(3) experimental max weight allowed within the acceptable range:", defective_experimental)
print("    theoretical Maximum weight:", defective_theoretical)
print("(4) experimental Probability that a product is neither premium nor defective:", nei_premium_nor_defective__experimental)
print("    theoretical Probability:", nei_premium_nor_defective__theoretical)