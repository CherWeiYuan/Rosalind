"""
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. 
       All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. 
       (Note: Only one solution will exist for the dataset provided.)
"""
import sys
from Bio.Seq import Seq

def splicing_translate(s, introns_list):
    for i in introns_list:
        if s.count(i) == 1:
            s = s.replace(i, "")
        else:
            print("Error: Intron detected more than once in the sequence.")
            sys.exit()
    return str(Seq(s).translate()[:-1])

from Bio import SeqIO
def splicing_translate_fasta(fasta): 
    # First sequence in fasta is s, the rest are substrings
    lst = []
    for sequence in SeqIO.parse(fasta, "fasta"):
        lst += [str(sequence.seq)]
    return splicing_translate(lst[0], lst[1:])

# Test case for splicing_translate()
s = "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG"
intron1 = "ATCGGTCGAA"
intron2 = "ATCGGTCGAGCGTGT"
splicing_translate(s, [intron1, intron2]) # expected output: MVYIADKQHVASREAYGHMFKVCA

# Test case for splicing_translate_fasta()
fasta = "rosalind_splc.fasta"
print(splicing_translate_fasta(fasta)) # expected output: MEDSHGTRSDFAHASLSGYGQVGTQGCQLGDSRYGTLELSTPRLQHGNVRHRDIQNTPNLDFDLPSPSPNLLSNGAWISLASAVLPGHLQSAAQRLEVLRGRIAGAECVEVIIGLICVGVEYSEIPLLVRMPRSPCFNERAIDLSNFKGGMILCCIFFRRNVSRSPWGLDTSVARKEAVTSIVCLVKQDPSGCPSLPSLSAASSSKTTD
