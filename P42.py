'''
Project Euler

Problem #42 - Coded triangle numbers

David 07/06/2017
'''

fileName = 'p042_words.txt'
file = open(fileName)
data = file.readlines()
words = data[0].split(',')
N = len(words)

triangle = [0]*25
for i in range(1,25):
    triangle[i]=i*(i+1)//2
print(triangle)

cnt = 0
for i in range(N):
    word = words[i]
    word = word.strip('"')
    summation = 0
    for char in word:
        summation += (ord(char)-64)
    if(summation in triangle):
        cnt += 1

print(cnt)
    
