'''
Project Euler

Problem #33 - Digit cancelling fractions

David 07/01/2017
'''

import time

def gcd(a,b): #greatest common divider
    if(b!=0):
        return gcd(b,a%b)
    else:
        return a
    
tic = time.time()
collect = []
# a/b where b>a
for a in range(10,100):
    setA = set(str(a))
    if(len(setA)==1):
        continue
    for b in range(a+1,100):
        setB = set(str(b))
        if(len(setB)==1):
            continue
        common_term = setA.intersection(setB)
        if(len(common_term)!=1): 
            continue
        else: # only one common digit
            setC = setA - common_term
            setD = setB - common_term
            c = int(setC.pop())
            if(c==0):
                continue
            d = int(setD.pop())
            if(d/c==b/a):
                if(common_term.pop()=='0'): # trivial example
                    pass
                else:
                    collect.append((a,b,c,d))
                    
print(collect)
numerator = 1
denominator = 1
for i in range(len(collect)):
    numerator *= collect[i][0]    # or numerator *= collect[i][2]
    denominator *= collect[i][1]   # or denominator *= collect[i][3]

divisor = gcd(numerator, denominator)
print(denominator//divisor)
    

toc = time.time()
print(toc-tic)
