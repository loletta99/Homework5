# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:52:37 2019

@author: Rosa
"""

def FASTA_parse(file):
    strings={}
    with open(file) as f:
        text=f.read()
        items=text.split('>')
    for item in items[1:]:
        item=item.split('\n')
        string_id=item.pop(0)
        strings[string_id]=''.join(item)
    return strings

def graph(s):
    s1 = s[0]
    k = ''
    res = ''
    for i in range(len(s1)):
        for j in range(i+1,len(s1)+1):
            k = s1[i:j]
            for h in range(1,len(s)):
                if k not in s[h]:
                    break
                if h + 1 == len(s) and len(res) < len(k):
                    if len(k)==3:
                        res= k
    return res