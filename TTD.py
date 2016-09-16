import pytest
import bioinfo_dicts

def n_neg(seq):
    """number of negative residues in a protein sequence"""
    seq = seq.upper()
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + 'is not a vaild aa.')

    return seq.count('D') + seq.count('E')
