'''
Project Euler

Problem #29 - Distinct powers

David 06/30/2017
'''

import math

s = set({})
for a in range(2,101):
    for b in range(2,101):
        s.add(a**b)

print(len(s))
