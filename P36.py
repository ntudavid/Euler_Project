'''
Project Euler

Problem #36 - Double-base palindromes

David 07/02/2017
'''

import math
import time

def dec2bin(decimal):
    binary = ''
    integerPart = int(decimal)
    fractionPart = decimal-integerPart
    # integer part
    while(integerPart!=0):
        binary = str(integerPart%2)+binary
        integerPart = integerPart//2
    # fractional part
    if(fractionPart!=0):
        binary = binary+'.'
        cnt = 0
        while(fractionPart!=0):
            cnt = cnt+1
            fractionPart = fractionPart*2
            if(fractionPart>=1):
                fractionPart = fractionPart-1
                binary = binary + '1'
            else:
                binary = binary + '0'
        #print(cnt) # 52
    return binary
    
def check_palindrome(string):
    rev_string = string[::-1]
    if(rev_string==string):
        return True
    else:
        return False

# main
tic = time.time()
up_bound = 1000000
summation = 0
for num in range(1,up_bound):
    if(check_palindrome(str(num))==True):
        bin_num = dec2bin(num)
        if(check_palindrome(bin_num)==True):
            summation += num

print(summation)
toc = time.time()
print(toc-tic)
              
            

