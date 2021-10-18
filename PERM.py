"""
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""
import math

def DFS(vertex, graph, path):
    new_path = path + [vertex]
    
    if len(new_path) == len(graph):
        new_path = list(str(x) for x in new_path)
        print(" ".join(new_path))
    
    for i in graph[vertex]:
        if i not in new_path:
            DFS(i, graph, new_path)
        
def perm(n):
    # Print total number of permutations
    print(math.factorial(n))
    
    # Make list of incremental numbers of length n
    lst = []
    for i in range(1,n+1):
        lst += [i]
    
    # Make graph, each vertex is connected to all vertex
    graph = {}
    for k in lst:
        graph[k] = list(filter(lambda y: y != k, lst))
    
    # Reset lst to save space
    lst = []
    
    # DFS at each starting vertex
    for start_vert in list(graph.keys()):
        path_start = []
        DFS(start_vert, graph, path_start)
    
perm(5)
