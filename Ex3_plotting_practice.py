#1
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
#import bootcamp_utils

rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

iptg = data_txt[:,0]
gfp = data_txt[:,1]
sem = data_txt[:,2]
#plot iptg vs gfp
plt.close()
# plt.semilogx(iptg, gfp, linestyle='none', marker='.',
#                     markersize=20)
# plt.title('IPTG Titration - semilog X')
# plt.xlabel('iptg (mM)')
# plt.ylabel('Normalized GFP')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# #plt.margins('0.2')
# plt.show()


plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.',
                    markersize=20)
plt.title('IPTG Titration - semilog X')
plt.xlabel('iptg (mM)')
plt.ylabel('Normalized GFP')
plt.ylim(-0.02, 1.02)
plt.xlim(8e-4, 15)
plt.xscale('log')

#plt.show()
