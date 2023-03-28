# 동전 0

import sys
sys.stdin = open('input.txt','r')

T, K = map(int,input().split())
a = []
cnt = 0
for t in range(T):
    num = int(input())
    a.append(num)

a = a[::-1]

for i in a:
    cnt += K//i
    K = K % i
print(cnt)