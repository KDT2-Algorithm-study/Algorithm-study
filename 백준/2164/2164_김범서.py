from collections import deque

num = int(input())
card = deque([i for i in range(1, num + 1)])

# 카드가 한 장 남을 때까지
# 가장 위에 있는 카드를 버리고
# 그 다음 가장 위에 있는 카드를 가장 아래로 옮긴다
while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

# 남은 카드의 번호를 출력한다
print(card.popleft())
