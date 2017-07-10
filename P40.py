'''
Project Euler

Problem #40 - Champernowne's constant

David 07/06/2017
'''

import math
import time


def d(n):
    index_bound = 0
    digit = 1
    while(n>index_bound+digit*9*10**(digit-1)):
        index_bound = index_bound+digit*9*10**(digit-1)
        digit += 1
        
    index = n-1-index_bound
    q = index//digit
    r = index%digit
    num = 10**(digit-1)+q
    str_num = str(num)
    return int(str_num[r])

# main
tic = time.time()

ans = d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000)
print(ans)

toc = time.time()
print(toc-tic)

                 

