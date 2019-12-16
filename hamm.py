# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:49:45 2019

@author: Rosa
"""

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
def ddd(s,t):
    s = list(s)
    t = list(t)
    count = 0
    for k in range(len(s)):
        if s[k] != t[k]:
            count += 1
    return count
print(ddd(s,t))