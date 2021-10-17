# ID: GC
# Q: Computing GC Content
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
# Sample output: Rosalind_0808 \n 60.919540

from Bio import SeqIO
from Bio.SeqUtils import GC

def compute_GC(fasta_file):
    id_lst = []
    seq_lst = []
    
    x = SeqIO.parse(fasta_file, "fasta")
    for i in x:
        id_lst += [i.id]
        seq_lst += [GC(i.seq)]
    
    max_GC = max(seq_lst)
    pos_max = seq_lst.index(max_GC)
    ID = id_lst[pos_max]
    GC_content = seq_lst[pos_max]
    
    print(ID)
    print(GC_content)
        

compute_GC("rosalind_gc.fasta")


# We can save space with the following code

def compute_GC_space(fasta_file):
    gc = 0
    ID = None
    
    x = SeqIO.parse(fasta_file, "fasta")
    for i in x:
        if GC(i.seq) > gc:
            ID = i.id
            gc = GC(i.seq)
    
    print(ID)
    print(gc)

compute_GC_space("rosalind_gc.fasta")
