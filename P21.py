'''
Project Euler

Problem #21 - Amicable numbers

David 06/29/2107
'''

import math

def d(num):
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
    #print(factors)
    #print(divisors)
    #print(cnt)
    multipliers = []
    for i in range(len(divisors)):
        multipliers.append(0)
        for j in range(cnt[i]+1):
            multipliers[-1] += divisors[i]**j
    #print(multipliers)
    d = 1
    for i in range(len(multipliers)):
        d *= multipliers[i]
    return d-originalNum


# main
summation = 0
for i in range(1,10001):
    j = d(i)
    if(i==d(j) and i!=j):
        summation += i

print(summation)


    

