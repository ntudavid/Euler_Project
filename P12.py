'''
Project Euler

Problem #12 - Highly divisible triangular number

David 06/27/2017
'''

import math
import time

def triangle_number(no):
    num =1
    for i in range(2,no+1):
        num += i
    return num

def decompose(num):
    primeFactors = []
    while(True):
        for i in range(2,int(num)+1):
            if(num%i==0):
                primeFactors.append(i)
                num = num/i
                break
        if(num==1):
            break       
    return primeFactors

def primeFactorize(num):
    factors = []
    while(True):
        sqroot = math.sqrt(num)
        bound = int(sqroot)+1
        prime = True
        for i in range(2,bound):
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
    return factors

def primeFactorize2(num): # speed_up version
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
    return factors

def count_divisors(factors):
    n = len(factors)
    if(n==0):
        return 2
    else:
        cnt = [1]
        for i in range(1,n):
            if(factors[i-1]!=factors[i]):
                cnt.append(1)
            else:
                cnt[-1] += 1
        divisorsN = 1
        for j in cnt:
            divisorsN *= j+1
        return divisorsN

# main
tic = time.time()
num = 1
while(True):
    tn = triangle_number(num)
    if(count_divisors(primeFactorize2(tn))>500):
        print(num)
        print(tn)
        break
    else:
        num +=1

toc = time.time()
print(toc-tic)
        
                
    
    
