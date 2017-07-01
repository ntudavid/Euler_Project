'''
Project Euler

Problem #26 - Reciprocal cycles

David 06/30/2017
'''

def recurring_cycle(num):
    if(num == 1):
        cnt = 0
    else:
        x = 9
        cnt = 1
        while(True):
            if(x%num==0):
                break
            else:
                x = 10*x+9
                cnt += 1
    return cnt

# main
recurring_cycle_list = [0]*1001
recurring_cycle_list[3]=1
for i in range(6,1001):
    num = i
    while(True):
        if(num%2==0):
            num = num//2
        elif(num%5==0):
            num = num//5
        else:
            break
    recurring_cycle_list[i] = recurring_cycle(num)

maxCycle = 1
maxNum = 3
for i in range(1001):
    cycle = recurring_cycle_list[i]
    if(cycle>maxCycle):
        maxCycle = cycle
        maxNum = i

print(maxNum, maxCycle)
    
