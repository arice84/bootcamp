import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#import scipy.stats
import bootcamp_utils as booU
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

df_weight = pd.read_csv('data/bee_weight.csv', comment='#')
df_sperm = pd.read_csv('data/bee_sperm.csv', comment='#')
#To remove NaN values
df_sperm = df_sperm[np.isfinite(df_sperm['Quality'])]

#generate data
# x_weight, y_weight =  booU.ecdf(df_weight.loc[
#     (df_weight['Treatment']=='Control'),'Weight'])
# x_weight, y_weight =  booU.ecdf(df_weight.loc[
#     (df_weight['Treatment']=='Pesticide'),'Weight'])
# x_sperm, y_sperm =  booU.ecdf(df_weight.loc[
#     (df_weight['Treatment']=='Control'),''])

#plot weight
plt.close()
def plot_ecdf(x, y):
    plt.plot(x, y, marker='.', linestyle='none', markersize=10, alpha=0.5)
    plt.ylabel('eCDF')

plot_ecdf(*(booU.ecdf(df_weight.loc[(df_weight['Treatment']=='Control'),'Weight'])))
plot_ecdf(*(booU.ecdf(df_weight.loc[(df_weight['Treatment']=='Pesticide'),'Weight'])))

plt.xlabel('drone weight')
plt.margins(0.02)
plt.legend(('control', 'Pesticide'), loc='lower right')
plt.title('drone weight')
#plt.show()

print('Mean drone weight: Control = ', df_weight.loc[
    (df_weight['Treatment']=='Control'),'Weight'].mean())
print('Mean drone weight: Pesticide = ', df_weight.loc[
    (df_weight['Treatment']=='Pesticide'),'Weight'].mean())

print('95 confidence drone weight: Control = ', booU.bs_conf_int(df_weight.loc[
    (df_weight['Treatment']=='Control'),'Weight'], np.mean))
print('95 confidence drone weight: Pesticide = ', booU.bs_conf_int(df_weight.loc[
    (df_weight['Treatment']=='Pesticide'),'Weight'], np.mean))



#plot sperm
plt.close()

plot_ecdf(*(booU.ecdf(df_sperm.loc[(df_weight['Treatment']=='Control'),'Quality'])))
plot_ecdf(*(booU.ecdf(df_sperm.loc[(df_weight['Treatment']=='Pesticide'),'Quality'])))

plt.xlabel('drone sperm')
plt.margins(0.02)
plt.legend(('control', 'Pesticide'), loc='lower right')
plt.title('drone sperm')

print('Mean drone sperm quality: Control = ', df_sperm.loc[
    (df_sperm['Treatment']=='Control'),'Quality'].mean())
print('Mean drone sperm quality: Pesticide = ', df_sperm.loc[
    (df_sperm['Treatment']=='Pesticide'),'Quality'].mean())

print('95 confidence drone sperm quality: Control = ', booU.bs_conf_int(df_sperm.loc[
    (df_sperm['Treatment']=='Control'),'Quality'], np.mean))
print('95 confidence drone sperm quality: Pesticide = ', booU.bs_conf_int(df_sperm.loc[
    (df_sperm['Treatment']=='Pesticide'),'Quality'], np.mean))

print('95 confidence drone sperm quality: Control = ', booU.bs_conf_int(df_sperm.loc[
    (df_sperm['Treatment']=='Control'),'Quality'], np.median))
print('95 confidence drone sperm quality: Pesticide = ', booU.bs_conf_int(df_sperm.loc[
    (df_sperm['Treatment']=='Pesticide'),'Quality'], np.median))

plt.show()
