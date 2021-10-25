"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
"""

# Paste RNA codon here
table = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V 
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

# Process RNA codon table into dictionary of codon: amino acid
table = table.split()
rna_codon = dict(zip(table[0::2], table[1::2]))

# Process dictionary of codon: amino acid to amino acid : number of codons
protein_codon_count = {}
for key, value in rna_codon.items():
    if value not in protein_codon_count.keys():
        protein_codon_count[value] = 1
    elif value in protein_codon_count.keys():
        protein_codon_count[value] += 1

# Visualize table of amino acid : number of codons
protein_codon_count

# Function to calculate number of codons possible in protein sequence modulo 1,000,000
from math import prod
def mRNA_num(prot_seq):
    num_lst = []
    # For every amino acid in prot_seq, add the number of RNA codon that codes for it in num_lst
    for aa in prot_seq:
        num_lst += [protein_codon_count[aa]]
    # Add number of stop codons to num_lst
    num_lst += [protein_codon_count['Stop']]
    
    # Return product of all numbers modulo 1,000,000
    return prod(num_lst)%1000000

mRNA_num('MA') # Expected output: 12
mRNA_num('MGWTFNVDFFLGYYWDVVAKIPPGGMRKMEWTMSKYYVVWWWFEMNYFYAAHVLYNVVNFLHWTLYREMPCLWIPARTSKTFLWAFMTKQNSFPPRVFEHLDPNERNFKEFVEGAECPASMSKNFEKEVEGSSPHGESEDWIVERNYYQLEFLTRRYPLWMHLTDHFTTIPIDVNMQKRHWFKLFDVWGIFCVPFHTIHGNVFRRKMYDCHDYPEAKWSNLCPKQAVQVYPVLFTGMVVEALTMDHDAVDQQWFCVRRCAMSVHDQTNQHPCMSFDSDMMAQISDKRHESWSKHDEKMRHRSLHCLFIVRDGMAADDGVFYKPKHWAMRMDCVGFEHERFLWAFKLPMCHFWTTARVIYYVMQDHINRPYNRQPMCPVFCICTNPKVRIDQNFNRADGGSEWEPTDAAGWRFLATSWSNLCTNSPELNGLVYPVYIPRKWFLLHDAFQHAIKRMKELMICYSQIIHPQMPIRSFGTCVNITFDKNNQVRSCNYPYKQSYVYGVQRHTHFSYCNDQMTHIWRYGQCIYCWEYMPSFFDQCYRNTNCDSVMLHVADVWIHVIDCYAFNATRSLTQPDMFEPNGCIGCFGIEQSMQASNNFPDFEKWEKWANIQNSMDHKCDINRKSNCKEWEAKPYNESGESAYDDKIRGFQRIIRSNKGFKDAFNENVPWGQLNDEAHPNWEADLQEFVDNSHFCLLAAADTWGVCKAYNGSLYKPFIEDWTRSRSREDVEYVSTTGQSVNVHDSGSFAAALQLKTPDDPQMMKWTMMHFDGNMFTHITFFDSKKVSYWCTFSANLESEKKGNPDHWQMGNMGWCCIRINNAQGHRYHLLDKGIFVRTFVKWTAVWEFYWYVDFKSHHRGFPAGTPRRWHGGKHTLRPTDDAQVEPVRLGTLMHGECCMKFACFRKKSIGRGWYLNCTQLQNLRCFLLFYQGWVSHDDLDTAIWRADMVPYYYWLKPQLPLPLDKFCWSGIYNLDRPARAECPCLYISCGDVHKNCNF') # Expected output: 324288
