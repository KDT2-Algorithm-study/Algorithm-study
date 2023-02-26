from collections import deque

n = int(input())
num = list(map(int,input().split()))
card = deque()
for i in range(1,n+1):
    j = num[-i]
    if j == 1:
        card.appendleft(i)
    elif j == 3:
        card.append(i)
    else:
        card.appendleft(i)
        if len(card)>1:
            card[0],card[1]=card[1],card[0]
print(*card)

# 늦어서 죄송합니다 ㅠ
