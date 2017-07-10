'''
Project Euler

Problem #37 - Truncatable primes

David 07/03/2017
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
cnt = 0
num = 23
while(True):
    if(isPrime(num)):
        str_num1 = str(num)
        str_num2 = str(num)
        digit = len(str_num1)
        truncatePrime = True
        for i in range(digit-1): # truncate digit-1 times
            str_num1 = str_num1[1:]
            if(isPrime(int(str_num1))==False):
                truncatePrime = False
                break
            str_num2 = str_num2[:-1]
            if(isPrime(int(str_num2))==False):
                truncatePrime = False
                break
        if(truncatePrime):
            collect.append(num)
            cnt += 1
    num += 2
    if(cnt==11):
        break

print(collect)
print(sum(collect))
toc = time.time()
print(toc-tic)
              
            

