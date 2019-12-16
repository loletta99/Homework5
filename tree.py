# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:58:40 2019

@author: Rosa
"""
with(open('rosalind_tree.txt', 'r')) as f:
    n = int(f.readline())
    t = [line.split() for line in f]

print(n - len(t) - 1)