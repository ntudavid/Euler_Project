'''
Project Euler

Problem #5 - Smallest multiple

David 06/27/2017
'''

import math

def isPrime(num):
    sqrt_num = math.sqrt(num)
    bound = int(sqrt_num)+1
    if(num==1):
        return False
    for i in range(2,bound):
        if(num%i==0):
            return False
    return True


# main
smallest_multiple = 1
for i in range(2,20+1):
    if(isPrime(i)):
        smallest_multiple *= i

smallest_multiple = smallest_multiple*(2**3)*(3)
print(smallest_multiple)
    
