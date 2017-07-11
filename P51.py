'''
Project Euler

Problem #51 - Prime digit replacements

David 07/10/2017
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

'''
Analysis:

only 1 * : impossible to have 8 family since there will be 3 number causing 3 multiple
2 repeating * : impossible with same reason above
Try the pattern with 3 repeating *

if 4-digit number: impossible ***1 (1111,5555 are not prime)
                              ***7 (2227,3337 are not prime)

Accordingly, try 5-digit and 6-digit numbers with 3 repeating *

'''

tic = time.time()

# Try 5-digit number
str_num = '0000'
digit0 = [1,3,7,9]
digit1 = list(range(9,-1,-1))

for m in range(4): # 0~3
    for i in digit1: # 4 cases
        for j in digit1:
            for k in digit0:
                cnt = 0
                for a in digit1:
                    num_list = [a]*5
                    num_list[m] = i
                    num_list[-1] = k
                    if(num_list[0]==0): # does not count
                        continue
                    num = 0
                    for b in range(5):
                        num += num_list[b]*10**(4-b)
                    if(isPrime(num)):
                        cnt +=1
                        if(cnt==8):
                            break
                if(cnt==8):
                    pattern = ['*']*5
                    pattern[m] = i
                    pattern[-1] = k
                    print(num,end=' ')
                    for c in range(5):
                        print(pattern[c],end='')
                    print()

# Try 6-digit number
str_num = '00000'
digit0 = [1,3,7,9]
digit1 = list(range(9,-1,-1))

for m in range(4): # 0~3
    for n in range(m+1,5): # m+1~4
        for i in digit1: # 4 cases
            for j in digit1:
                for k in digit0:
                    cnt = 0
                    for a in digit1:
                        num_list = [a]*6
                        num_list[m] = i
                        num_list[n] = j
                        num_list[-1] = k
                        if(num_list[0]==0): # does not count
                            continue
                        num = 0
                        for b in range(6):
                            num += num_list[b]*10**(5-b)
                        if(isPrime(num)):
                            cnt +=1
                            if(cnt==8):
                                break
                    if(cnt==8):
                        pattern = ['*']*6
                        pattern[m] = i
                        pattern[n] = j
                        pattern[-1] = k
                        print(num,end=' ')
                        for c in range(6):
                            print(pattern[c],end='')
                        print()

toc = time.time()
print(toc-tic)
