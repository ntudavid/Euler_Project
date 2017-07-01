'''
Project Euler

Problem #14 - Longest Collatz sequence

David 06/28/2017
'''

import time

def collatz(num):
    cnt = 1
    while(num!=1):
        cnt += 1
        if(num%2==0):
            num = num/2
        else: # odd number
            num = 3*num+1
    return cnt

# main
tic = time.time()
N = 1000000
longestChain = 1
startingNum = 1
for i in range(1,N):
    chain_length = collatz(i)
    if(chain_length>longestChain):
        longestChain = chain_length
        startingNum = i

print(startingNum)
toc = time.time()
print(toc-tic)


