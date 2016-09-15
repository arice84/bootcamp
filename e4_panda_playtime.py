import numpy as np
import pandas as pd

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# FI = df.loc[(df['ID']=='I'), ['impact force (mN)']]
# np.mean(FI['impact force (mN)'])
frog_list = ['I','II','III','IV']
mean_impf = np.empty(len(frog_list))

for i, frog in enumerate(frog_list):
    FI = df.loc[(df['ID']==frog), ['impact force (mN)']]
    mean_impf[i] = np.mean(FI['impact force (mN)'])

#now with group by
# We only want ID's and impact forces, so slice those out
df_impf = df.loc[:, ['ID', 'impact force (mN)']]

# Make a GroupBy object
grouped = df_impf.groupby('ID')

# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)

# Look at the new DataFrame
df_mean_impf
