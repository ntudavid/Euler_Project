'''
Project Euler

Problem #30 - Digit fifth powers

David 06/30/2017
'''

digit = 5
up_bound = (digit+1)*9**digit
fifth_powers = []
for i in range(2,up_bound):
    str_num = str(i)
    summation = 0
    for d in str_num:
        term = int(d)**digit
        summation += term
    if(summation==i):
        print(i)
        fifth_powers.append(i)

print(sum(fifth_powers))
