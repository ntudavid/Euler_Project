'''
Project Euler

Problem #48 - Self powers

David 07/09/2017
'''

import time

tic = time.time()

num = 0
for i in range(1,1001):
    num += i**i

str_num = str(num)
print(len(str_num))
print(str_num[-10:])    

toc = time.time()
print(toc-tic)


    

