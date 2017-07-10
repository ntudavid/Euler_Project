'''
Project Euler

Problem #39 - Integer right triangles

David 07/05/2017
'''

import math
import time

# main
tic = time.time()
max_cnt = 0
max_p = 120
for p in range(3,1001):
    bound1 = p//3
    bound2 = p//2
    cnt = 0
    for i in range(1,bound1):
        for j in range(i,bound2):
            k = p-i-j
            if(i+j<k):
                continue
            else:
                if(i**2+j**2==k**2):
                    cnt += 1
    if(cnt>max_cnt):
        max_cnt = cnt
        max_p = p

print(max_p,max_cnt)
toc = time.time()
print(toc-tic)
              
            

