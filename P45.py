'''
Project Euler

Problem #45 - Triangular, pentagonal, and hexagonal

David 07/07/2017
'''

import time
import math

def triangle(num):
    n=(math.sqrt(1+8*num)-1)/2
    if(int(n)==n):
        return int(n)
    else:
        return 0

def pentagon(num):
    n=(1+math.sqrt(1+24*num))/6
    if(int(n)==n):
        return int(n)
    else:
        return 0

def hexagonal(num):
    n=(math.sqrt(1+8*num)+1)/4
    if(int(n)==n):
        return int(n)
    else:
        return 0
    
# main
tic = time.time()

n = 1
cnt = 0
while(cnt<3):
    Hn = n*(2*n-1)
    if((triangle(Hn)>0) and (pentagon(Hn)>0)):
        print(Hn)
        cnt += 1
    n += 1

toc = time.time()
print(toc-tic)


