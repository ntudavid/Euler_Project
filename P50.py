'''
Project Euler

Problem #50 - Consecutive prime sum

David 07/09/2017
'''

import time
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


# main
tic = time.time()

primeCollect = [2]
num = 3
bound = 1000000
while(num<bound):
    if(isPrime(num)):
        primeCollect.append(num)
    num += 2

N = len(primeCollect)
consecutiveDigits = 1
while(True):
    summation = 0
    for i in range(consecutiveDigits):
        summation += primeCollect[i]
    if(summation>=bound):
        consecutiveDigits -= 1
        break
    else:
        consecutiveDigits += 1
    
#print(consecutiveDigits)

while(True):   
    idx = 0
    prime = 2
    for i in range(N-consecutiveDigits+1):
        summation = sum(primeCollect[i:i+consecutiveDigits])
        if(summation<bound and isPrime(summation)):
            idx = i
            prime = summation
    if(prime==2):
        consecutiveDigits -= 1
    else:
        break

print(idx,consecutiveDigits,prime)

toc = time.time()
print(toc-tic)


    

