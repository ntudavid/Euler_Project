'''
Project Euler

Problem #4 - Largest palindrome product

David 06/27/2107
'''

x = range(100,1000)
y = range(100,1000)
largestPalindrome = 100*100+1
for i in x:
    for j in y:
        num = i*j
        # check palindrome
        reverse_num = int(str(num)[::-1])
        if(num-reverse_num==0):
            if(num>largestPalindrome):
                largestPalindrome = num

print(largestPalindrome)
    
