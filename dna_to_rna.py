def rna(seq):
    """
    convert dna sequence to RNA
    """

    seq = seq.upper()

    return seq.replace('T','U')
