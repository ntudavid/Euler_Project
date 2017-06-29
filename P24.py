'''
Project Euler

Problem #24 - Lexicographic permutations

David 06/29/2107
'''

import math

numbers = ['0','1','2','3','4','5','6','7','8','9']
N = len(numbers)
No = 1000000
num = No-1
permutation = []
for i in range(N,0,-1): # 10 9 8 7 6 5 4 3 2 1
    f = math.factorial(i-1) # f9 f8 f7 f6 f5 f4 f3 f2 f1 f0
    d = num//f
    sel = numbers[d]
    permutation.append(sel)
    numbers.remove(sel)
    num = num - d*f
print(permutation)

    

