# 베스트셀러

import sys
sys.stdin = open('input.txt','r')

T = int(input())

dick = {}

for _ in range(T):
    word = input()
    if word not in dick:
        dick[word] = 1
    else:
        dick[word] = dick[word] + 1
    
a = []

for key,value in dick.items():
    if max(dick.values()) == value:
        a.append(key)

b = sorted(a)
print(b[0])

