from collections import deque

card = deque(range(1,int(input())+1))

while len(card) > 1:
    card.popleft()
    card.rotate(-1) # 카드가 한장이 남을 때까지 한장빼고 한장뒤로넘기고를 반복
print(*card) # 마지막 한장 출력 !