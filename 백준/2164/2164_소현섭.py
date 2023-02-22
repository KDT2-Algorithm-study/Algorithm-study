import sys
from collections import deque

card = deque([x for x in range(1, int(sys.stdin.readline())+1)])
while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
print(card[0])