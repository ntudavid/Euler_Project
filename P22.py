'''
Project Euler

Problem #21 - Amicable numbers

David 06/29/2017
'''

fileName = 'p022_names.txt'
file = open(fileName)
data = file.readlines()
names = data[0].strip().split(',')
names.sort()
N = len(names)
scores = [0]*N
for i in range(N):
    name = names[i]
    name = name.strip('"')
    summation = 0
    for char in name:
        summation += (ord(char)-64)
    scores[i] = summation*(i+1)
    
print(sum(scores))
