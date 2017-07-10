'''
Project Euler

Problem #47 - Distinct primes factors

David 07/09/2017
'''

import time
import math

def decompose(num):
    originalNum = num
    factors = []
    while(True):
        prime = True
        if(num%2==0):
            prime = False
            factors.append(2)
            num = num/2
        else:
            sqroot = math.sqrt(num)
            bound = int(sqroot)+1
            for i in range(3,bound,2):
                if(num%i==0):
                    prime = False
                    factors.append(i)
                    num = num/i
                    break
        if(prime):
            factors.append(int(num))
            num = num/num
        if(num==1):
            break
        
    # sum of all divisors less then num
    divisors = [factors[0]]
    cnt = [1]
    for i in range(1,len(factors)):
        if(factors[i]!=factors[i-1]):
            divisors.append(factors[i])
            cnt.append(1)
        else:
            cnt[-1] += 1
    return divisors, cnt


# main
tic = time.time()

distinctDigit = 4
isFind = False
num = 4
while(isFind==False):
    isFind = True
    for i in range(distinctDigit):
        if(len(decompose(num+i)[0])!=distinctDigit):
            isFind = False
            num += i+1
            break

print(num)    

toc = time.time()
print(toc-tic)


    

