'''
Project Euler

Problem #23 - Non-abundant sums

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
# perfect number : d(num)==num
# deficient number : d(num)<num
# abundant number : d(num)>num

collect_abundant_nums = []
for i in range(12,28123):
    if(d(i)>i):
        collect_abundant_nums.append(i)

bound = 28123
n = len(collect_abundant_nums)
two_abundant_sum = [False]*bound
for i in range(n):
    a = collect_abundant_nums[i]
    for j in range(i,n):
        b = collect_abundant_nums[j]
        if(a+b)<bound:
            two_abundant_sum[a+b] = True

summation = 0
for i in range(1,bound):
    if(two_abundant_sum[i]==False):
        summation += i
print(summation)



    

