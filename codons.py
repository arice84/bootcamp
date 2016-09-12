codon = input("input your codon please:")
codon_list = ['UAA', 'UAG', 'UGA']
if codon == 'AUG':
    print("this is a start codon")
elif codon in codon_list:
    print("this is a stop codon")
else:
    print("this isn't either start or stop")
