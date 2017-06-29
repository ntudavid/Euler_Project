'''
Project Euler

Problem #19 - Counting Sundays

David 06/29/2107
'''

def isLeapYear(y):
    if(y%400==0):
        return True
    elif(y%100==0):
        return False
    elif(y%4==0):
        return True
    else:
        return False

def calendar(year,month,date):
    dayList = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    dateCntList = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    dateCntLeap = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    yearBase = 1900
    dateBase = 1
    dayBase = 1 # Monday

    dateCnt = 0
    # year
    for y in range(1900, year):
        if(isLeapYear(y)):
            dateCnt += 366
        else:
            dateCnt += 365
    # month
    if(isLeapYear(year)):
        for m in range(1,month):
                dateCnt += dateCntLeap[m]
    else:
        for m in range(1,month):
                dateCnt += dateCntList[m]
    # date
    dateCnt += date-dateBase
    # infered day
    day = (dateCnt+dayBase)%7
    return dayList[day]

# main
cnt = 0
for y in range(1901,2001):
    for m in range(1,13):
        if(calendar(y,m,1)=='Sunday'):
            cnt += 1
print(cnt)

