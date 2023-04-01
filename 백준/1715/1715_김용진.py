# 카드 정렬하기

import sys,heapq
sys.stdin = open('input.txt','r')

T = int(input())
card_list = []
cnt = 0
for t in range(T):
    heapq.heappush(card_list,int(input()))

for i in range(len(card_list)-1):
    num = heapq.heappop(card_list) + heapq.heappop(card_list)
    cnt += num
    heapq.heappush(card_list, num)
print(cnt)