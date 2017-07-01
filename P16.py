'''
Project Euler

Problem #16 - Power digit sum

David 06/28/2017
'''

import time
import numpy as np


p = 1000
str_num = str(2**p)
list_num = list(str_num)
summation = 0
for i in list_num:
    summation += int(i)
print(summation)

