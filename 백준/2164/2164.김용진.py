# 카드2
import sys
sys.stdin = open('input.txt','r')

from collections import deque
T = int(input())
card = deque()
for i in range(1,T+1):
    card.append(i)
if len(card) != 1:
    while 1:
        card.popleft()
        card.append(card.popleft())  
        if len(card) == 1:
            break
print(*card)