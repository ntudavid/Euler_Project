'''
Project Euler

Problem #2 - Even Fibonacci numbers

David 06/27/2017
'''

noExceed = 4000000
fab1 = 1
fab2 = 2
fab = fab1 + fab2
summation = 2
while(fab<=noExceed):
    if(fab%2==0):
        summation += fab
    fab1 = fab2
    fab2 = fab
    fab = fab1 + fab2

print(summation)
