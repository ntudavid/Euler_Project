'''
Project Euler

Problem #31 - Coin sums

David 07/01/2017
'''

import time

def H1(val):
    return 1

def H2(val):
    scenarios = val//2
    cnt = 0
    for i in range(scenarios+1):
        cnt += H1(val-2*i)
    return cnt

def H3(val):
    scenarios = val//5
    cnt = 0
    for i in range(scenarios+1):
        cnt += H2(val-5*i)
    return cnt


def H4(val):
    scenarios = val//10
    cnt = 0
    for i in range(scenarios+1):
        cnt += H3(val-10*i)
    return cnt

def H5(val):
    scenarios = val//20
    cnt = 0
    for i in range(scenarios+1):
        cnt += H4(val-20*i)
    return cnt

def H6(val):
    scenarios = val//50
    cnt = 0
    for i in range(scenarios+1):
        cnt += H5(val-50*i)
    return cnt

def H7(val):
    scenarios = val//100
    cnt = 0
    for i in range(scenarios+1):
        cnt += H6(val-100*i)
    return cnt

def H8(val):
    scenarios = val//200
    cnt = 0
    for i in range(scenarios+1):
        cnt += H7(val-200*i)
    return cnt

# main
dollars = 200
tic = time.time()
print(H8(dollars))
toc = time.time()
print(toc-tic)
