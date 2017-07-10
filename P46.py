'''
Project Euler

Problem #46 - Goldbach's other conjecture

David 07/09/2017
'''

import math
import time

def isOddPrime(num):
    if(num<=1):
        return False
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

num = 9
while(True):
    conjecture = False
    if(isOddPrime(num)):
        conjecture = True
    else:
        square = 1
        while(True):
            ts = 2*square**2
            if(num<=ts):
                break
            else:
                if(isOddPrime(num-ts)):
                    conjecture = True
                    break
                else:
                    square +=1

    if(conjecture):
        num += 2
    else:
        break

print(num)

toc = time.time()
print(toc-tic)
              
            

