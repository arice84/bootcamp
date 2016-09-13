"""homework exercise 2"""

import os
import warnings

def concat_strings(a,b, **kwargs):
    """concatenate strings"""
    seq = a+b
    for key in kwargs:
        seq += kwargs[key]
    return seq

#Ex 2.2b
def read_fasta(fasta_file):
    with open(fasta_file, 'r') as f:
        seq_str = []
        for line in f.readlines():
            if line[0] != '>':
                seq_str.extend(line.rstrip())
            else:
                header = line
    return ''.join(seq_str), header

#Ex 2.3
def gc_content(seq):
    """calculates the gc content of a sequence"""
    seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)

def gc_blocks(seq, block_size):
    """divides sequence into blocks of given size and computes GC content for
    each block"""
    block_list = []
    step = 0
    for i in range(len(seq)//block_size):
        block_list.append(seq[step:step+block_size])
        step += block_size
#    print(block_list)

    #calculate GC Content
    gc_list = []
    for block in block_list:
        gc_list.append(gc_content(block))
    return tuple(gc_list), block_list

def gc_map(seq, block_size, gc_thresh):
    """displays sequnce with blocks that have gc content above threashold as all
    caps. Non-overlapping blocks of length = block_size."""

    gc_list, block_list = gc_blocks(seq, block_size)
    mapped_list = []
    important_list = []
    for i, block in enumerate(block_list):
        if gc_list[i] > gc_thresh:
            mapped_list.append(block.upper())
            important_list.append((i, gc_list[i]),)
        else:
            mapped_list.append(block.lower())
    print(important_list)
    return ''.join(mapped_list)

def write_mapped_file(in_file, out_file, block_size=1000, gc_thresh=0.4):
    """opens, maps, and writes map to a file showing areas of high GC content in
    input fasta file. Outputs fasta file with native header."""
    seq, header = read_fasta(in_file)
    mapped_seq = gc_map(seq, block_size, gc_thresh)

    if os.path.isfile(str(out_file)):
        raise RunTimeError('%s already exists, will not write to it' % str(outfile))

    with open(str(out_file), 'w') as f:
        f.write(str(header))
        for i in range(len(mapped_seq)//60):
            f.write(mapped_seq[i*60:60+i*60] + '\n')
        f.write(mapped_seq[i*60:60+i*60])
    
