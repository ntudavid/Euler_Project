'''
Project Euler

Problem #32 - Pandigital products

David 07/01/2017
'''

import time

tic = time.time()
collect = set({})
for i in range(1,1000):
    for j in range(i+1,10000):
        cnt = [0]*10
        prod = i*j
        for ch in str(i):
            cnt[int(ch)] += 1
        for ch in str(j):
            cnt[int(ch)] += 1
        for ch in str(prod):
            cnt[int(ch)] += 1

        if(cnt[0]>0):
            continue
        else:
            allChecked = True
            for k in range(1,10):
                if(cnt[k]!=1):
                    allChecked = False
                    break
            if(allChecked):
                collect.add(prod)
                print(i,' x ',j,' = ',prod)
        
print(sum(collect))

toc = time.time()
print(toc-tic)
