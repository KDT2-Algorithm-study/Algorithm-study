# 팩토리얼

import sys
sys.stdin = open('input.txt','r')

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

num = int(input())
print(factorial(num))
