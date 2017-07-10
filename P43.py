'''
Project Euler

Problem #43 - Sub-string divisibility

David 07/06/2017
'''

import time

def checkDivisible(string):
    divisors = [1,2,3,5,7,11,13,17]
    divisible = True
    for i in range(1,8):
        num = int(string[i:i+3])
        if(num%divisors[i]!=0):
            divisible = False
            break
    return divisible
    
summation = 0

def permutate(arr,n):
    if(n==len(arr)):
        #print(arr)
        str_num = ''
        for j in range(n):
            str_num += str(arr[j])
        if(checkDivisible(str_num)):
            global summation
            summation += int(str_num)
            print(str_num)
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

arr = list(range(0,10))
permutate(arr,0)

print(summation)

toc = time.time()
print(toc-tic)


