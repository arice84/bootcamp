import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#import scipy.stats
import bootcamp_utils as booU
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

#munging
#new column names and columns
new_names = ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']
df_1973 = df_1973.rename(columns={'yearband': 'year',
                                'beak length': 'beak length (mm)',
                                'beak depth': 'beak depth (mm)'})
df_1973['year'] = pd.Series(1973, index=df_1973.index)
df_1975 = df_1975.rename(columns={'Beak length, mm': 'beak length (mm)',
                                'Beak depth, mm': 'beak depth (mm)'})
df_1975['year'] = pd.Series(1975, index=df_1975.index)
df_1987 = df_1987.rename(columns={'Beak length, mm': 'beak length (mm)',
                                'Beak depth, mm': 'beak depth (mm)'})
df_1987['year'] = pd.Series(1987, index=df_1987.index)
df_1991 = df_1991.rename(columns={'blength': 'beak length (mm)',
                                'bdepth': 'beak depth (mm)'})
df_1991['year'] = pd.Series(1991, index=df_1991.index)
df_2012 = df_2012.rename(columns={'blength': 'beak length (mm)',
                                'bdepth': 'beak depth (mm)'})
df_2012['year'] = pd.Series(2012, index=df_2012.index)

#combine data into one DataFrame
df = pd.concat((df_1973, df_1975, df_1987, df_1991, df_2012), ignore_index=True)

df.to_csv('grant_complete_AR.csv', index=False)

#4.1.c
df_non_redundant = df.drop_duplicates(subset=['year', 'band'])

#4.1.d
#plotting data
plt.close()
plt.figure()
plt.subplot(2,1,1)
x_fort, y_fort = booU.ecdf(df_non_redundant.loc[
    (df_non_redundant['year']==1987) & (df_non_redundant['species']=='fortis'),
    'beak depth (mm)'])
x_scan, y_scan = booU.ecdf(df_non_redundant.loc[
    (df_non_redundant['year']==1987) & (df_non_redundant['species']=='scandens'),
    'beak depth (mm)'])
plt.plot(x_fort, y_fort, marker='.', linestyle='none',
                        markersize=10, alpha=0.5)
plt.plot(x_scan, y_scan, marker='.', linestyle='none',
                        markersize=10, alpha=0.5)
plt.xlabel('beak depth (mm)')
plt.ylabel('eCDF')
plt.legend(('fortis', 'scandens'), loc='lower right')
plt.title('1987')
plt.margins(0.02)

#length
plt.subplot(2,1,2)
x_fort_len, y_fort_len = booU.ecdf(df_non_redundant.loc[
    (df_non_redundant['year']==1987) & (df_non_redundant['species']=='fortis'),
    'beak length (mm)'])
x_scan_len, y_scan_len = booU.ecdf(df_non_redundant.loc[
    (df_non_redundant['year']==1987) & (df_non_redundant['species']=='scandens'),
    'beak length (mm)'])
plt.plot(x_fort_len, y_fort_len, marker='.', linestyle='none',
                        markersize=10, alpha=0.5)
plt.plot(x_scan_len, y_scan_len, marker='.', linestyle='none',
                        markersize=10, alpha=0.5)
plt.xlabel('beak length (mm)')
plt.ylabel('eCDF')
plt.legend(('fortis', 'scandens'), loc='lower right')
plt.margins(0.02)

plt.tight_layout()
plt.show()
