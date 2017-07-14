'''
Project Euler

Problem #53 - Combinatoric selections

David 07/14/2017
'''

import time

def nchoosek(n,k):
    if(n<k):
        return 0
    elif(k==0):
        return 1
    else: # n>=k
        #lookup = np.zeros((n+1,k+1),np.int64)
        lookup = []
        for i in range(n+1):
            lookup.append([0]*(k+1))
        # initial conditions
        for i in range(n+1):
            lookup[i][0] = 1
            lookup[i][1] = i
        for j in range(k+1):
            lookup[j][j] = 1
        # complete the talbe
        for i in range(1,n+1):
            for j in range(1,k+1):
                if(i>j):
                    lookup[i][j] = lookup[i-1][j] + lookup[i-1][j-1]
                else:
                    break
        #print(lookup)
        return lookup[n][k]


tic = time.time()
low_bound = 1000000
cnt = 0

for n in range(1,101):
    for r in range(n//2+1):
        ans = nchoosek(n,r)
        if(ans>low_bound):
            if(r==n/2):
                cnt += 1
            else:
                cnt += 2    # symmetic property


print(cnt)
toc = time.time()
print(toc-tic)
