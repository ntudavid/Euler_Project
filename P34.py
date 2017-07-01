'''
Project Euler

Problem #34 - Digit factorials

David 07/01/2017
'''

import math
import time

tic = time.time()

fact = []
for i in range(10):
    fact.append(math.factorial(i))

# for a 7-digit number, the sum of its digit factorials is 9!*7 (7-digit) the max.
# suppose there is a number that is greater than 9!*7 and is equal to sum of digit factorials
# it is impossible because the sum of digit factorials for such 7-digit number cannot exceed 9!*7
up_bound = math.factorial(9)*7
collect = []
for num in range(10,up_bound):
    str_num = str(num)
    summation = 0
    for ch in str_num:
        summation += fact[int(ch)]
    if(summation == num):
        collect.append(num)

print(collect)
print(sum(collect))
    
toc = time.time()
print(toc-tic)







