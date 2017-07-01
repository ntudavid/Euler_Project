'''
Project Euler

Problem #1 - Multiples of 3 and 5

David 06/27/2017
'''

def sum_of_multiples_3_5_below(num):
    summation = 0
    for i in range(2,num):
        if((i%3==0) or (i%5==0)):
            summation += i
    return summation


# main
num = 1000
print(sum_of_multiples_3_5_below(num))
