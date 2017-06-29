'''
Project Euler

Problem #3 - Largest prime factor

David 06/27/2107
'''
import math
import time

def find_largest_prime_factor(num):
    largestPrimeFactor = num
    while(True):
        for i in range(2,int(num)+1):
            if(num%i==0):
                largestPrimeFactor = i
                num = num/i
                break
        if(num==1):
            break       
    return largestPrimeFactor


def find_largest_prime_factor2(num):
    largestPrimeFactor = int(num)
    while(True):
        sqroot = math.sqrt(num)
        bound = int(sqroot)+1
        prime = True
        for i in range(2,bound):
            if(num%i==0):
                prime = False
                num = num/i
                break
        if(prime):
            largestPrimeFactor = int(num)
            num = num/num
        if(num==1):
            break     
    return largestPrimeFactor


# main
tic = time.time()
num = 600851475143
print(find_largest_prime_factor2(num))
toc = time.time()
print(toc-tic)
