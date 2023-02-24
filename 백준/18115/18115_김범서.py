from collections import deque

n = int(input())
order = list(map(int, input().split()))
result = deque()

for i in range(1, n + 1):
    # 뒤로가기
    now = order.pop()
    # 기술 1: 가장 위에 있는 것을 카드 뭉치 가장 위에 옮긴다
    if now == 1:
        result.appendleft(i)
    # 기술 2: 가장 위에 있는 것을 카드 뭉치의 위에서 두 번째 자리로 옮긴다
    elif now == 2:
        temp = result.popleft()
        result.appendleft(i)
        result.appendleft(temp)
    # 기술 3: 가장 위에 있는 것을 카드 뭉치 가장 아래로 옮긴다
    elif now == 3:
        result.append(i)

print(*result)
