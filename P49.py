'''
Project Euler

Problem #49 - Prime permutations

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

def checkPerm(L):
    num1 = list(str(L[0]))
    num2 = list(str(L[1]))
    num3 = list(str(L[2]))
    num1.sort()
    num2.sort()
    num3.sort()
    same = True
    for i in range(4):
        if(num1[i]!=num2[i] or num1[i]!=num3[i]):
            same = False
            break
    return same

# main
tic = time.time()

digit_4_prime = []
for num in range(1000,10000):
    if(isPrime(num)):
        digit_4_prime.append(num)
N = len(digit_4_prime)
#print(N)
for i in range(N-2):
    for j in range(i+1,N-1):
        diff = digit_4_prime[j]-digit_4_prime[i]
        prime3 = digit_4_prime[j]+diff
        if(prime3<=10000 and isPrime(prime3)):
            checkSet = [digit_4_prime[i],digit_4_prime[j],digit_4_prime[j]+diff]
            if(checkPerm(checkSet)):
                print(checkSet)

toc = time.time()
print(toc-tic)


    

