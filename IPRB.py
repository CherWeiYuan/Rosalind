'''
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.'
'''

# Approach: Generate probability tree. Use Depth-First-Search (DFS) algorithm to explore all vertices in the tree.
#           There will be three layers in tree: 1 (start) --> first parent --> second parent (* probability of having offspring with >= 1 "A", where applicable)
#           First parent layer is represented by specific strings, which are keys to dictionary (tree in script)
#           The keys from first parent layer will access the probabilities of third layer
#           Before multiplying all vertices in a branch, we use dic to convert string in second layer to probabilities
#           DFS will search the entire tree to enumerate all multiplied probabilities at each branch, and all of them will be added together to return the desired answer

from fractions import Fraction as F
from math import prod

# Depth-First-Search algorithm to transverse all vertices in tree
def DFS(vertex, tree, p_list, sum_list, dic): 
    # deepcopy p_list so that new_p_list is unlinked to p_list
    new_p_list = []
    for i in p_list:
        new_p_list += [i]
    new_p_list += [vertex]
    
    # End recursion if new_p_list has three vertices
    if len(new_p_list) == 3:
        new_p_list[1] = dic[new_p_list[1]]
        new_p_list[2] = dic[new_p_list[2]]
        sum_list += [prod(new_p_list)]
        return None
    
    # If not, explore all edges in tree
    else:
        for new_vertex in tree[vertex]:
            DFS(new_vertex, tree, new_p_list, sum_list, dic)

# Mendel's First Law function
def MFL(k, m, n):
    # Set up dictionary to access the probability at each vertex
    dic =  {"pK": F(k,(k+m+n)), # p(AA) as fraction so calculation is exact
            "pM": F(m,(k+m+n)), # p(Aa) as fraction so calculation is exact
            "pN": F(n/(k+m+n)), # p(aa) as fraction so calculation is exact
            "AA": F(k,(k+m+n-1)),
            "AA_": F(k-1,(k+m+n-1)), # for AA --> AA
            "Aa": F(m,(k+m+n-1)),
            "aa": F(n,(k+m+n-1)),
            "Aa_": F(m-1,(k+m+n-1)) * F(3, 4), # for Aa --> Aa --> x3/4
            "aa_": 0, # for aa --> aa --> x0
            "aa*": F(n,(k+m+n-1)) * F(1,2), # for Aa --> aa --> x1/2
            "Aa*": F(m,(k+m+n-1)) * F(1,2) # for aa --> Aa --> x1/2
            }
    
    # Set up graph tree
    tree = { 1: ["pK", "pM", "pN"],    
            "pK": ["AA_", "Aa", "aa"], # second layer of branches start with "_"
            "pM": ["AA", "Aa_", "aa*"],
            "pN": ["AA", "Aa*", "aa_"]}    
    
    # Explore all vertices in tree using Depth-First-Search algorithm
    p_list = []
    sum_list = []
    DFS(1, tree, p_list, sum_list, dic)
    
    return round(float(sum(sum_list)), 5)

MFL(2,2,2)
MFL(28, 25, 24)








