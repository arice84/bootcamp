import pytest
import bioinfo_dicts
import numpy as np

def find_codon(codon, seq):
    """Find a specified codon with a given sequence."""
    seq = seq.upper()
    codon = codon.upper()

    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 1

    if i == len(seq):
        return -1

    return i

import scipy.optimize

def gradient_model(x, I_0, a, lam):
    if np.any(np.array(x) < 0):
        raise RuntimeError('x must be positive')
    if np.any(np.array([I_0, a, lam] < 0)):
        raise RuntimeError('all params must be positive')
    return a + I_0 * np.exp(-x / lam)
