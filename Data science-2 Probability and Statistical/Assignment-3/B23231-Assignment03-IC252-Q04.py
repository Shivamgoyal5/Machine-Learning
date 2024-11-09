import numpy as np

# Calculate the theoretical probability of getting a full house in poker
denominator = np.math.comb(52, 5)
numerator = np.math.comb(13, 1) * np.math.comb(4, 3) * np.math.comb(12, 1) * np.math.comb(4, 2)
probability_theoretical = numerator / denominator
print("The theoretical probability of getting a full house in poker:", probability_theoretical)

# Simulate the experiment
num_simulations = 100000
full_house_count = 0

for _ in range(num_simulations):
    deck = list(range(1, 14)) * 4  # Representing card ranks 1 to 13, each repeated 4 times for the four suits
    hand = np.random.choice(deck, size=5, replace=False)  # Deal 5 cards without replacement
    ranks, counts = np.unique(hand, return_counts=True)
    
    if 3 in counts and 2 in counts:  # Check if the hand forms a full house
        full_house_count += 1

probability_experimental = full_house_count / num_simulations
print("The experimental probability of getting a full house in poker:", probability_experimental)  



# Part (c): Probability of getting at least 2 full houses in 1000 trials

#theoretical
#getting full house 0 times
p1=1-probability_theoretical#probability of not getting ful house
a1=1
for i in range(1000):
    a1=a1*p1
#getting full house 1 times    
a2=1
for i in range(999):
    a2=a2*p1
a2=1000*a2*probability_theoretical
final_prob=1-a1-a2
print(final_prob)


#experimental
num_trials = 1000
num_full_houses = 0
num_simulations1=1000

for _ in range(num_trials):
    full_house_count_trial = 0
    for _ in range(num_simulations1):
        deck = list(range(1, 14)) * 4
        hand = np.random.choice(deck, size=5, replace=False)
        ranks, counts = np.unique(hand, return_counts=True)
        if 3 in counts and 2 in counts:
            full_house_count_trial += 1
    if full_house_count_trial >= 2:
        num_full_houses += 1

at_least_2_full_houses_probability = num_full_houses / num_trials
print("Probability of getting at least 2 full houses in 1000 trials:", at_least_2_full_houses_probability)

# Calculate mean and variance
mean = num_full_houses / num_trials
variance = np.var([1 if np.random.binomial(1, probability_experimental) else 0 for _ in range(num_trials)])

print("Mean:", mean)
print("Variance:", variance)
