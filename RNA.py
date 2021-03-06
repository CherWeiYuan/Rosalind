# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:19:58 2021

@author: cherw
"""

"""
ID: DNA
Q: Transcribing DNA into RNA

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

"""

test1 = "GATGGAACTTGACTACGTAAATT"
test2 = "GACTTGAATAACGGAACAATTCTTCCCGATGCCAAAGGTTGGATGATCTCTGCCCGAATACGGAGTACCATGGCTCCAGAAACTATTAGCTCCTATCCGTACCTGGAAGTAACGCTCATTCCAAGCATTCTGGCGTGGTGCAGTAATCACACGAAGTACTTCCCTTACGCTAGACAGGCGCAGCACAAAGCTGTCTGGTATGCTAGATGATACCCGTCTTTGGTACCAAGCAGTGCGATATGCATTCTTACTCGGAGGGAGCGATCGGCGGATATAGTAGAGGAGAGATCGCAAAATTTACGGGCCACCTTCTGCATGAAATGGATCTGGCTAATTCTTCGGGTCCGAACTTATTCTTTGGTACCGTGTTCTTAGCTATGTCGGTGAGGTTCATTTTAAGATCAGCCTTTGGTTTCTTAGCTGTAGTAAGCTAGCGGCTCGTGGATCCGGATTCCCGATGCATCTCCACGCCCATGGGAGAAGGATGTCCGTCATTATAAAGATGGCCCGTTAGTAACTGGCTGCACTCTTTCGATAGCGGTCCCATGTTAAAGTGACCCCAGTCGCGGGTTTATGCTCTAATTCTGTGCGGCGCGCCGGGGGCGTTGGATCCTCGCCCTCTGCCACGAAAGGCTGACAAGTTCAACCTCGTATAAGCGTTACCCCGTAGCGCCCATGTTGAACTGACTGAGTGTCCGGTGATTTAGTGTGGTCGCGACCAAGTATTGGCTGCTTACCCGTAATGCTTACCCCTTTAGTTCGTTGCTCTCAACCGAGGGAACGCTTTAGTGCGGCTGGGGGTAGTGTGCCCTCTTAACCGTTCAACTGCTCTGGCTATTTCGCGTTCTAACAAGTTACGCCATCCTATTCAACGCGTTGGTTCACAGATCACCCATAATCCTGGGAGGCTTCTTGAATCTCGATTCTAGCTGGAAGA"

def transcribe(t):
    # O(n) = O(len(t))
    x = t.replace("T", "U")
    return x
    
transcribe(test2)


