'''
Project Euler

Problem #7 - 10001st prime

David 06/27/2107
'''


import math

def isPrime(num):
    if(num==1):
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
no = 10001
cnt =0
number = 1
while(cnt < no):
    number += 1
    if(isPrime(number)):
        cnt += 1

print(number)
