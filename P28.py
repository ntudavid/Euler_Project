'''
Project Euler

Problem #28 - Number spiral diagonals

David 06/30/2017
'''


summation = 1
size = 1001
x = 1
for i in range(3,size+1,2):
    for j in range(4):
        x += i-1
        summation += x

print(summation)
