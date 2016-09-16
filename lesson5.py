import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#import scipy.stats
import bootcamp_utils as booU
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

sns.boxplot(data=df, x='ID', y ='impf')
plt.gca().legend_.remove()
