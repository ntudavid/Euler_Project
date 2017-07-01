'''
Project Euler

Problem #27 - Quadratic primes

David 06/30/2017
'''

import math

def isPrime(num):
    if(num<=1):
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


def quadraticPrime(a,b):
    n = 0
    while(True):
        p = n**2+a*n+b
        if(isPrime(p)):
            n += 1
        else:
            break
    return n-1
    

# main

maxN = 1
maxA = 0
maxB = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = quadraticPrime(a,b)
        if(n>maxN):
            maxN = n
            maxA = a
            maxB = b
print(maxN)
#print(maxA)
#print(maxB)
print(maxA*maxB)

