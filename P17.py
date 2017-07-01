'''
Project Euler

Problem #17 - Number letter counts

David 06/28/2017
'''

import time
import numpy as np


# one two three four five six seven eight nine ten
# eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty
# twenty thirty forty fifty sixty seventy eighty ninety

number_in_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                   'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                   'seventeen', 'eighteen', 'nineteen']
cnt19 = [0]
for num in number_in_words:
    cnt19.append(len(num))

tens_in_words = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

cnt20 = [0, 0]
for num in tens_in_words:
    cnt20.append(len(num))

def count_words(num):
    cnt = 0
    if(num<=19):
        cnt = cnt19[num]
    elif(num<100):
        ten_digit = num//10
        first_digit = num%10
        cnt = cnt20[ten_digit]+cnt19[first_digit]
    elif(num<1000):
        hundred_digit = num//100
        cnt += cnt19[hundred_digit]+7 # hundred(7)
        remainder = num%100
        if(remainder!=0):
            cnt += 3  # and(3)
        if(remainder<=19):
            cnt += cnt19[remainder]
        else:
            ten_digit = remainder//10
            first_digit = remainder%10
            cnt += cnt20[ten_digit]+cnt19[first_digit]
    else: # over 999
        pass
    return cnt

# main
summation = 0
for i in range(1,1000):
    summation += count_words(i)

summation += 11  # one thousand
print(summation)




