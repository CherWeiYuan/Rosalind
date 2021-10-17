# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 12:52:27 2021

@author: cherw
"""

'''
ID: FIB
Q: Rabbits and Recurrence Relations

A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2–√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent the n-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if Fn represents the number of rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

'''

def fib_loop(n, k):
    # Time: O(n)
    # Space: O(1)
    newborn = 1
    reproducing = 0
    total = 0
    if n == 0:
        return 0
    for i in range(1, n+1):
        total = reproducing + newborn
        newborn = k * reproducing
        reproducing = total
    return total

fib_loop(5,3)

def fib_recur(n, k):
    # Time: For every call, there are two calls spawning. O(2**n)
    # Space: O(n)
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n == 3:
        return 1 + k
    else:
        return fib_recur(n-1, k) + k*fib_recur(n-2, k)

fib_recur(3,3)

# Try recursion with caching to avoid making the same calculations

def fibocache_recur(n, k):
    cache = {}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    if (n, k) not in cache:
        cache[(n,k)] = fibocache_recur(n-1,k) + k*fibocache_recur(n-2,k)
    return cache[(n,k)]

fibocache_recur(6,3)


def stress_test(a):
    import random
    while True:
        x = random.randint(0, a)
        y = random.randint(0, a)
        print(f'n = {x}, k = {y}')
        
        print("Running loop algorithm")
        ans_loop = fib_loop(x, y)
        
        print("Running recursion with cache")
        ans_recur_cache = fibocache_recur(x, y)
        
        #print("Running recursion algorithm")
        #ans_recur = fib_recur(x, y)
        
        if ans_loop != ans_recur_cache:
            print(f"Answer from recur: {ans_recur}; Answer from loop: {ans_loop}")
            break


# Test using small numbers    
stress_test(10)

# Test using large numbers
stress_test(40)
# Any larger and recursion takes forever to run
    


















