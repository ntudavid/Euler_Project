'''
Project Euler

Problem #15 - Lattice paths

David 06/28/2107
'''

import time
import numpy as np

def nchoosek(n,k):
    if(n<k):
        return 0
    elif(k==0):
        return 1
    else: # n>=k
        lookup = np.zeros((n+1,k+1),np.int64)
        for i in range(n+1):
            lookup[i,0] = 1
            lookup[i,1] = i
        for j in range(k+1):
            lookup[j,j] = 1
        # complete the talbe
        for i in range(1,n+1):
            for j in range(1,k+1):
                if(i>j):
                    lookup[i,j] = lookup[i-1,j] + lookup[i-1,j-1]
                else:
                    break
        #print(lookup)
        return lookup[n,k]
    

# main
tic = time.time()
print(nchoosek(40,20))
toc = time.time()
print(toc-tic)


