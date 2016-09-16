import numpy as np
import scipy.optimize

def gradient_model(x, I_0, a, lam):
    if np.any(np.array(x) < 0):
        raise RuntimeError('x must be positive')
    if np.any(np.array([I_0, a, lam] < 0)):
        raise RuntimeError('all params must be positive')
    return a + I_0 * np.exp(-x / lam)
