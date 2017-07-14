'''
Project Euler

Problem #52 - Permuted multiples

David 07/14/2017
'''

import time

tic = time.time()
num = 10
while(True):
    isFound = True
    originalSet = set(str(num))
    # check mulitple 2 3 4 5 6
    for i in range(2,7):
        numX = num*i
        anotherSet = set(str(numX))
        #diffSet = (originalSet-anotherSet).union((anotherSet-originalSet))
        diffSet = originalSet^anotherSet  # symmetric_difference()
        if(len(diffSet)!=0):
            isFound = False
            break
    if(isFound):
        print(num)
        break
    else:
        num += 1

toc = time.time()
print(toc-tic)
