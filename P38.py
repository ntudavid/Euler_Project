'''
Project Euler

Problem #38 - Pandigital multiples

David 07/05/2017
'''

import math
import time

def check_pandigital(s):
    if(len(s)!= 9):
        return False
    else:
        cnt = [0]*10
        for i in range(9):
            cnt[int(s[i])] += 1
        pandigital = True
        for j in range(1,10):
            if(cnt[j]!=1):
                pandigital = False
                break
        return pandigital

# main
tic = time.time()

max_pandigital = 123456789
for n in range(2,9): # n>=2
    # if n==2 : i can be large as a 4 digit number, 5 digit number is impossible s
    for i in range(2,10000): 
        str_num =  ''
        for j in range(1,n+1):
            str_num += str(i*j)
        if(check_pandigital(str_num)):
            #print(i,n,str_num)
            num = int(str_num)
            if(num>max_pandigital):
                max_pandigital = num
            
print(max_pandigital)

toc = time.time()
print(toc-tic)
              
            

