#如何拥有无穷力量
#递归
"""
1.base case - a straight point
not defined in terms of itself
smallest input
2.recursive case
defined in terms of smaller version
"""

#factorial
def factorial(n):
    if n==0:
        return 1
    if n>0:
        return n*factorial(n-1)

#palindromes
def is_palindroms(s):
    if s=='':
        return True
    else:
        if s[0]==s[-1]:
            return is_palindroms(s[1:-1])
        else:
            return False

def iter_palindroms(s):
    for i in range(0,len(s)/2):
        if s[i]!=s[-(i+1)]:
            return False
        return True

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#my answer
def fast_fibonacci(n):
    if n==0: return 0
    if n==1: return 1
    a=[]
    a.append(0)
    a.append(1)
    i=2
    while i<=n:
        a.append(a[i-1]+a[i-2])
        i+=1
    return a[i-1]

#standard answer
"""
def fibonacci(n):
    current = 0 
    after = 1
    for i in range(0,n):
        current, after = after, current + after
    return current
"""

#网页排名
#受欢迎程度转化成递归
#relaxation algorithm
#start with a guess
#while not done:
#    make the guess better



