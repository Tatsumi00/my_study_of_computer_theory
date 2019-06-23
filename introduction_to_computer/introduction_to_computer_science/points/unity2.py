#解决问题的方法
#0.理解问题

#1.possible inputs
#生日，当前日期，检查

#2.outputs
#生日天数

#3.examples to understand relationship
#3.5consider systematically how a human solves the problem
#分日分月分年

#4.simple mechanical solution
#试着先从简单开始

#5.单元测试

#nextDay  从简单开始，假设每月30天,最后解决
"""
def nextDay(year, month, day):
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    # YOUR CODE HERE
    if month==12&day==30:
        return year+1,1,1
    if day==30:
        return year,month+1,day
    return year,month,day+1
    """

#daysBwtweenDates
def dateIsBefore(year1,month1,day1,year2,month2,day2):
    if year1<year2:
        return True
    if year1 ==year2:
        return True
    if month1 == month2:
        return day1<day2
    return False

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    days=0
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
        year1,month1,day1=nextDay(year1,month1,day1)
        days+=1
    return days

def nextDay(year,month,day):
    if year%4==0 & year%100!=0:
        if month==2:
            if day<29:
                return year,month,day+1
            else:
                return year,month+1,1
        if month==12:
            if day<31:
                return year,month,day+1
            else:
                return year+1,1,1
        if month in (1,3,5,7,8,10):
            if day<31:
                return year,month,day+1
            else:
                return year,month+1,1
        if month in (4,6,9,11):
            if day<30:
                return year,month,day+1
            else:
                return year,month+1,1
    else:
        if month==2:
            if day<28:
                return year,month,day+1
            else:
                return year,month+1,1
        if month==12:
            if day<31:
                return year,month,day+1
            else:
                return year+1,1,1
        if month in (1,3,5,7,8,10):
            if day<31:
                return year,month,day+1
            else:
                return year,month+1,1
        if month in (4,6,9,11):
            if day<30:
                return year,month,day+1
            else:
                return year,month+1,1




