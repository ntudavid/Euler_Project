'''
Project Euler

Problem #22 - Names scores

David 06/29/2017
'''

import time

tic = time.time()

fileName = 'p022_names.txt'
file = open(fileName)
data = file.readlines()
names = data[0].strip().split(',')
names.sort()
N = len(names)
score = 0
for i in range(N):
    name = names[i]
    name = name.strip('"')
    summation = 0
    for char in name:
        summation += (ord(char)-64)
    score += summation*(i+1)
    
print(score)

toc = time.time()
print(toc-tic)
