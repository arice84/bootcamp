"""lesson funcitons"""
def complement(base, material="DNA"):
    """returns the complement of a basepair"""

    if base in 'Aa':
        if material == "DNA":
            return "T"
        elif material =="RNA":
            return "U"
        else:
            raise RuntimeError("invaild materia")
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq, material='DNA'):
    """compute the reverse complement of a nucleic acid sequence"""

    #initalize empty sequence
    rev_comp = ''

    #
    for base in reversed(seq):
        rev_comp += complement(base, material=material)
    return rev_comp
