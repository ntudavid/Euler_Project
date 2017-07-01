'''
Project Euler

Problem #6 - Sum square difference

David 06/27/2017
'''

# approach #1
summation = 0
num = 100
for i in range(1,num+1):
    for j in range(i+1,num+1):
        summation += i*j

print(2*summation)
    

# approach #2
s1 = 0
s2 = 0
for i in range(1,num+1):
    s1 += i
    s2 += i*i
ans = s1**2 -s2
print(ans)
    
