'''
Project Euler

Problem #26 - Reciprocal cycles

David 06/30/2107
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
is_prime = [False]*1001
check_list = [True]*1001
for i in range(1001):
    if(isPrime(i)):
        is_prime[i]=True
        check_list[i]=False
check_list[2]=True
check_list[5]=True

recurring_cycle = [0]*1001
x = 9
cnt = 1
while(True):
    #print(cnt)
    for i in range(1001):
        if(check_list[i]==False):
            if(x%i==0):
                check_list[i]=True
                recurring_cycle[i]=cnt
            
    # check every num if it is checked
    done = True
    for j in range(1001):
        if(check_list[j]==False):
            done = False
            break
    if(done==True):
        break
    else:
        x = 10*x+9
        cnt += 1

maxNum = 0
maxIndex = 0
for i in range(1001):
    if(recurring_cycle[i]>maxNum):
        maxNum = recurring_cycle[i]
        maxIndex = i

#print(maxNum)
print(maxIndex)



