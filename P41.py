'''
Project Euler

Problem #41 - Pandigital prime

David 07/06/2017
'''

import time
import math

maxPandigitalPrime = 2

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


def permutate(arr,n):
    if(n==len(arr)):
        #print(arr)
        str_num = ''
        for j in range(n):
            str_num += str(arr[j])
        num = int(str_num)
        if(isPrime(num)):
            global maxPandigitalPrime
            if(num>maxPandigitalPrime):
                maxPandigitalPrime = num
    else:
        for i in range(n,len(arr)):
            # swap index n(head), i
            temp = arr[i]
            arr[i] = arr[n]
            arr[n] = temp
            permutate(arr,n+1)
            # swap back to resume arr
            temp = arr[i]
            arr[i] = arr[n]
            arr[n] = temp


# main
tic = time.time()
for digit in range(2,9):
    arr = list(range(1,digit+1))
    permutate(arr,0)

print(maxPandigitalPrime)
toc = time.time()
print(toc-tic)


