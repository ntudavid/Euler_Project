'''
Project Euler

Problem #20 - Factorial digit sum

David 06/29/2107
'''

import math

f100 = math.factorial(100)
f100_list = list(str(f100))
summation = 0
for digit in f100_list:
    summation += int(digit)
print(summation)
