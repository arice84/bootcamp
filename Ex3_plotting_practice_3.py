import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import bootcamp_utils as booU

rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

#load data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

x_high, y_high = booU.ecdf(xa_high)
x_low, y_low = booU.ecdf(xa_low)

x = np.linspace(1600, 2500, 400)
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))

plt.close()
plt.plot(x_high, y_high, marker='.', linestyle='none',
                        markersize=20, alpha=0.5)
plt.plot(x_low, y_low, marker='.', linestyle='none',
                        markersize=20, alpha=0.5)

plt.xlabel('cross sectional area (um)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc='lower right')

plt.plot(x, cdf_high, color='grey')
plt.plot(x, cdf_low, color='grey')
plt.show()
