# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:40:33 2019

@author: Rosa
"""
def pdst(string1, string2):
    result = 0
    for i in range(0, len(string1)):
        if(string1[i] != string2[i]):
            result += 1
    return result

def FastaReaderStringsOnly(strFileName):
    resultList = []
    resultString = ''
    with open(strFileName) as f:
        for line in f:
            if ('>' in line):
                if (resultString != ''):
                    resultList.append(resultString)
                    resultString = ''
            else:
                resultString = resultString + line.strip()
        if (resultString != ''):
            resultList.append(resultString)
    return resultList

strings = FastaReaderStringsOnly("rosalind_pdst.txt")
ln = len(strings)
st = strings[0]
ln_string = len(st)

matrix = [[0 for x in range(ln)] for y in range(ln)] 

for i in range(0, ln):
    for j in range(0, i):
        matrix[i][j] = pdst(strings[i], strings[j])/ln_string 
        matrix[j][i] = matrix[i][j]

f = open('DistanceMatrix.txt', 'w')
line = ""
for i in range(0, ln):
    for j in range(0, ln):
        line = line + str(matrix[i][j]) + '\t'
    f.write(line)
    f.write('\n')
    line = ""
f.close() 