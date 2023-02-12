# 피보나치 함수
import sys
sys.stdin = open('input.txt','r')

T = int(input()) 

for i in range(T):
    a = [1] 
    b = [0]
    num = int(input())
    for x in range(num):    
        b.append(a[x] + b[x])
        a.append(b[x])
    print(a[-1],b[-1])