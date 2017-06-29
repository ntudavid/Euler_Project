'''
Project Euler

Problem #25 - 1000-digit Fibonacci number

David 06/29/2107
'''

import time

def fib(n):
    f0 = 0
    f1 = 1
    if(n==0): # F(0)
        f = f0
    elif(n==1): # F(1)
        f = f1
    else: # F(2)...
        f = f0+f1
        cnt = 2
        while(cnt<n):
            f0 = f1
            f1 = f
            f = f0+f1
            cnt += 1
    return f


# main
tic = time.time()
digit = 1000
cnt = 0
while(True):
    cnt += 1
    f = fib(cnt)
    str_f = str(f)
    if(len(str_f)==digit):
        print(cnt)
        break
toc = time.time()
print(toc-tic)
            
