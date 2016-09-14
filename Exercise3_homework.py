import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import bootcamp_utils as booU

#import bootcamp_utils

rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

#load data
fc_wt = np.loadtxt('data/wt_lac.csv', comments='#', skiprows=3, delimiter=',')
fc_18m = np.loadtxt('data/q18m_lac.csv', comments='#', skiprows=3, delimiter=',')
fc_18a = np.loadtxt('data/q18a_lac.csv', comments='#', skiprows=3, delimiter=',')
data_list = [fc_wt, fc_18a, fc_18m]
RK_tup = (141.5, 16.56, 1328.)


#generate data
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """calculate fold change from iptg conc, RK, and optional parameter args"""
    numer = RK * (1+(c/KdA))**2
    denom = (1+(c/KdA))**2 + Kswitch * (1 + (c/KdI))**2
    fc = (1 + (numer/denom))**-1
    return fc

def fold_change_bohr(bohr_parameter):
    """calculate fold change from the bohr parameter"""
    fcB = 1 / (1 + np.e**(-bohr_parameter))
    return fcB

def calc_bohr_param(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """calculate bohr parameter from iptg conc"""
    numer = (1+(c/KdA))**2
    denom = (1+(c/KdA))**2 + Kswitch * (1 + (c/KdI))**2
    bohr_param = (-np.log(RK)) - np.log(numer/denom)
    return bohr_param

#plot experimental data
# legend = ()
# plt.close()
# for experiment, data in enumerate(data_list):
#     iptg = data[:,0]
#     fc = data[:,1]
#     x = np.logspace(-6, 2, 400)
#     y = fold_change(x, RK_tup[experiment])
#     #plot data
#     plt.semilogx(iptg, fc, marker='.', linestyle='none',
#                         markersize=20, alpha=0.5)
#     plt.plot(x, y, color='grey')
#     plt.xlabel('IPTG (mM)')
#     plt.ylabel('fold change')
#     # legend += (str(data,)
#     plt.legend(('fc_wt', 'fc_18m', 'fc_18a'), loc='lower right')
# plt.title('Fold change repression - semilogx')
#plt.show()

##plot collapsed data
plt.close()
bohr_x = np.linspace(-6, 6, 400)
bohr_y = fold_change_bohr(bohr_x)

plt.plot(bohr_x, bohr_y, color='black')

for experiment, data in enumerate(data_list):
    iptg = data[:,0]
    fc = data[:,1]
    x = calc_bohr_param(iptg, RK_tup[experiment])
    y = fold_change_bohr(x)
    #plot data
    plt.plot(x, fc, marker='.', linestyle='none',
                        markersize=20, alpha=0.5)
    plt.xlabel('bohr parameter (mM)')
    plt.ylabel('fold change')
    # legend += (str(data,)
plt.legend(('bohr_curve','fc_wt', 'fc_18m', 'fc_18a'), loc='lower right')
plt.title('Collapsed data')

#plt.show()
