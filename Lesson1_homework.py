"""Lesson 1 homework"""
#Ex 1.3
def reverse_comp(DNA):
    """returns a string with reverse complement of the string argument DNA
    sequence"""
    rev_dna = DNA[::-1]
    new_dna = []
    for i, element in enumerate(rev_dna):
        if element in 'Gg':
            new_dna.extend('c')
        elif element in 'Cc':
            new_dna.extend('g')
        elif element in 'Uu':
            new_dna.extend('a')
        elif element in 'Aa':
            new_dna.extend('u')
        else:
            print('this is not a basepair',element, i)
    return ''.join(new_dna)

def reverse_comp2(DNA):
    """returns a string with reverse complement of the string argument DNA
    sequence"""
    rev_dna = DNA[::-1].lower()
    rev_comp = rev_dna.replace('t', 'x')
    rev_comp = rev_comp.replace('a', 't')
    rev_comp = rev_comp.replace('x', 'a')
    rev_comp = rev_comp.replace('c', 'x')
    rev_comp = rev_comp.replace('g', 'c')
    rev_comp = rev_comp.replace('x', 'g')
    print(rev_comp)

#Ex 1.4
"""two options:
1. intersection of sets which is good for small sequences
2. slow break down which is good for longer sequences --> choice
"""

def find_seq(template, query):
    """find sequence in another.
    Input string template and tuple of queries.
    Output list of matches. """
    matches = []
    for seq in query:
        if seq in template:
            matches.append(seq)
#    print('find_seq', matches)
    return matches

def shatter_seq(seq, size):
    """shatters a sequnce into fragments of length = size.
    Output list of fragments."""
    fragments = []
    i = 0
    while i+size <= len(seq):
        fragments.append(seq[i:i+size])
        i += 1
#    print('shatter', fragments)
    return fragments

def size_seq(seq1, seq2):
    """identify the largest and smallest sequence. Output tuple of big and
    sequence.
    """
    if len(seq1) >= len(seq2):
        big, little = seq1, seq2
    else:
        big, little = seq2, seq1
    return big, little

def match_list(seq1, seq2):
    """identifies and outputs a the longest common subsequence between two
    argument sequences."""
    big, little = size_seq(seq1,seq2)
    size = len(little)
    matches_1 = []
#    matches_2 = []
    while size > 1 and len(matches_1) == 0: #and len(matches_2) == 0:
        matches_1 = find_seq(big, shatter_seq(little, size))
#        matches_2 = find_seq(little, shatter_seq(big, size))
        size -= 1
#    return list(set(matches_1 + matches_2))
    return matches_1

def substring_finder(seq1, seq2):
    """formats output of identified substrings"""
    seq1 = seq1.lower()
    seq2 = seq2.lower()
    matches = match_list(seq1, seq2)
    if len(matches) == 0:
        print("there were no matching substrings larger than 2 basepairs")
    elif len(matches) == 1:
        print("the largest match was %d basepairs: %s" % (len(matches[0]), ''.join(matches[0])))
    else:
        print("there were %d matches of equal length:" % len(matches), ', '.join(matches))

#Ex 1.5
def equal_para(struct):
    """compares the number of '(' and ')' and makes sure they're equal.
    Return bool True is ok and False is not a valid structure."""
    if struct.count('(') == struct.count(')'):
        return True
    else:
        return False

def dotparen_to_bp(struct):
    """generates a list of tuples representing locations of para pairs."""
    open_sites = []
    close_sites = []
    for site, identity in enumberate(struct):
        if identity == '(':
            open_sites.append(site)
        elif identity == ')':
            close_sites.append(site)
        else:
            pass
    return open_sites, close_sites

def join_sites(struct):
    """make single list of tupled sites"""
    open_sites, close_sites = dotparen_to_bp(struct)
    site_list = []
    for site1, site2 in zip(open_sites, close_sites):
        site_list.append((site1,site2)
    return tuple(site_list)

def pin_sizer(site_tuple):
    """test list of sites for proper hairpin sizes"""
    min_diff = 0
    for element in site_tuple:
        s1, s2 = element
        if s2-s1 < min_diff:
            min_diff = s2-s1
    if min_diff < 4:
        return False
    elif min_diff > 4:
        return True
        
###Incomplete. See answers for much shorter solutions.
