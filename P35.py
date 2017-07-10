'''
Project Euler

Problem #35 - Quadratic primes

David 07/02/2017
'''

import math
import time

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

# main
tic = time.time()
collect = []
for num in range(2,1000000):
    if(isPrime(num)):
        str_num = str(num)
        digit = len(str_num)
        circularPrime = True
        for i in range(digit-1): # rotate digit-1 times
            str_num = str_num + str_num[0]
            str_num = str_num[1:]
            if(isPrime(int(str_num))==False):
                circularPrime = False
                break
        if(circularPrime):
            collect.append(num)

print(collect)
print(len(collect))
toc = time.time()
print(toc-tic)
              
            

