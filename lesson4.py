import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import bootcamp_utils as booU

x = np.random.random(size=100000)
x_ecdf, y_ecdf = booU.ecdf(x)
plt.plot(x_ecdf[::1000], y_ecdf[::1000], marker='.', linestyle='none', markersize=10)

x = np.random.random(size=20)
heads = x <=0.5
