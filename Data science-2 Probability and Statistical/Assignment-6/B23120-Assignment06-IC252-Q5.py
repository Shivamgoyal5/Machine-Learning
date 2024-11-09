import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def stats(sample):
    mean = np.mean(sample)
    std_dev = np.std(sample)
    return mean, std_dev

def plot(ax:plt.axes, sample, idx, n):
    ax.hist(sample, bins=30, density=True, alpha=0.5, label='Sample '+str(idx))
    ax.set_title(f'N= {n}')
    ax.set_ylabel('Frequency')


mean = 65
std_dev = 15

# initialise norm:
norm_dist = norm(loc=mean, scale=std_dev)

# part a:
sample_size = 50
def part_a(sample_size, ax):
    print('N: ', sample_size)
    samples = [norm_dist.rvs(size=sample_size) for i in range(5)]

    # plot actual:
    x = np.linspace(20, 120, 1000)
    ax.plot(x, norm_dist.pdf(x), 'k--', lw=2, label='Actual')


    for i, sample in enumerate(samples):
        print('Sample', i+1)
        mean, std_dev = stats(sample)
        print(f'\tSample Mean: {mean:.3f}')
        print(f'\tSample Standard Deviation: {std_dev:.3f}')
        plot(ax, sample, i+1, sample_size)

    plt.legend()

fig, ax = plt.subplots()
part_a(sample_size, ax)
plt.show()


# part b:
sample_sizes = [100, 150, 250]
fig, axis = plt.subplots(3, 1, figsize=(10, 15))
for i, sample_size in enumerate(sample_sizes):
    part_a(sample_size, axis[i])
    print('\n\n')
plt.show()

# part c:

# to be continued...