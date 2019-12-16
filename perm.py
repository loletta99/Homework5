# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:15:51 2019

@author: Rosa
"""

import math                                         
import itertools                                    
n = 7                                               
print(math.factorial(n))                            
perm = itertools.permutations(list(range(1, n + 1)))
for i, j in enumerate(list(perm)):                  
    permutation = ''                                
    for item in j:                                  
        permutation += str(item) + ' '              
    print(permutation) 