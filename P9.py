'''
Project Euler

Problem #9 - Special Pythagorean triplet

David 06/27/2017
'''

def pythagorean(num):
    for a in range(1,int(num/3)):
        for b in range(a+1,int(num/2)):
            c = num - a - b
            if(c<b):
                break
            if(c**2-a**2-b**2==0):
                return a*b*c

# main
print(pythagorean(1000))
