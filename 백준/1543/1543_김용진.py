# 문서 검색

import sys,heapq
sys.stdin = open('input.txt','r')

word = input()
find = input()
num = 0
cnt = 0
i = len(find)

while len(word) >= i:
   if word[num:i] == find:
        cnt += 1
        i += len(find)
        num += len(find)
   else:
        i += 1
        num += 1

print(cnt)

