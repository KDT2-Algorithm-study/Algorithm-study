# 간단한 소인수분해

import sys
sys.stdin = open('input.txt','r')

def simple(x):
    number = 2
    while number <= x:
        if x % number == 0:
            a.append(number)
            x = x / number
        else:
            number = number + 1


num = int(input())

for i in range(1,num+1):
    a = []
    simple(int(input()))
    print(f'#{i} {a.count(2)} {a.count(3)} {a.count(5)} {a.count(7)} {a.count(11)}')