"""bootcamp utilities a collection of functions that are useful in bootcamp"""
import numpy as np

def ecdf(data):
    """compute x, y values for an empirical distribution function"""
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)
    return x, y

def bootstrap(data_array, np_stat, reps):
    """
    calculate bootstrap values for for given data and statistic
    return array of data values
    """
    #initalize an empty array for replicates
    bs_reps = np.empty(reps)
    for i in range(reps):
        bs_sample = np.random.choice(data_array, replace=True, size=len(data_array))
        bs_reps[i] = np_stat(bs_sample)
    return bs_reps

def bs_conf_int(data_array, np_stat, reps=100000, interval=[2.5,97.5]):
    """
    calculate confidence interval of bootstrap replicates of given dataset.
    """
    bs_reps = bootstrap(data_array, np_stat, reps)
    return  np.percentile(bs_reps, interval)
