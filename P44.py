'''
Project Euler

Problem #44 - Pentagon numbers

David 07/07/2017
'''

import math
import time

def pentagon(num):
    n=(1+math.sqrt(1+24*num))/6
    if(int(n)==n):
        return int(n)
    else:
        return 0

# main
tic = time.time()

k = 1
minD = float('inf')
cnt = 0
while(True):
    if((3*k-2)>minD):
        break
    else:
        Pk = k*(3*k-1)//2
        for j in range(k-1,0,-1):
            Pj = j*(3*j-1)//2
            s = Pk+Pj
            if(pentagon(s)>0):
                d = Pk-Pj
                if(pentagon(d)>0):
                    print(j,k,d)
                    if(d<minD):
                        minD = Pk-Pj
                    break
    k+=1
    
print(k)
print(minD)
toc = time.time()
print(toc-tic)

# Results
'''
1020 2167 5482660
52430 91650 8476206790
95506 110461 4620347250
111972 121168 3215928562
73745 129198 16880669542
'''
