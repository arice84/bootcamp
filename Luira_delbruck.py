import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#import scipy.stats
#import bootcamp_utils as booU

#specfiy parameters
#number of generations
n_gen = 16

#chance of having benefitial mutatation
r = 1e-5

#total number of cells
n_cells = 2**(n_gen -1)

#adaptive immuinity samples

ai_samples = np.random.binomial(n_cells, r, size=100000)

print('AI mean', np.mean(ai_samples))


def draw_random_mutation(n_gen, r):
    """Draw sample under random mutaition hyp"""
    n_mut = 0
    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)
    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    samples = np.empty(size)
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)
    return samples
