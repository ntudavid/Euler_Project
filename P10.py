'''
Project Euler

Problem #10 - Summation of primes

David 06/27/2017
'''

import math
import time

def isPrime(num):
    sqrt_num = math.sqrt(num)
    bound = int(sqrt_num)+1
    if(num==1):
        return False
    for i in range(2,bound):
        if(num%i==0):
            return False
    return True

def isPrime2(num):
    if(num==1):
        return False
    elif(num==2):
        return True
    elif(num%2==0):
        return False
    else:
        sqrt_num = math.sqrt(num)
        bound = int(sqrt_num)+1
        for i in range(3,bound,2):
            if(num%i==0):
                return False
        return True

# main
tic = time.time()
num_below = 2000000
summation = 0
for i in range(2,num_below):
    if(isPrime2(i)):
        summation += i

print(summation)
toc = time.time()
print(toc-tic)
