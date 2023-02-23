from collections import deque

n, m = map(int, input().split())
# 뽑아내려는 수의 위치
number = deque([x for x in range(1, n + 1)])
# 큐
target = deque(map(int, input().split()))
cnt = 0

while target:
    # 뽑아야 할 원소가 가장 앞에 있을 때
    # 원소를 뽑는다
    if target[0] == number[0]:
        number.popleft()
        target.popleft()
    # 뽑아야 할 원소가 앞부터 가운데 사이에 있을 때
    elif number.index(target[0]) <= len(number) // 2:
        while True:
            number.rotate(-1)
            cnt += 1
            if target[0] == number[0]:
                break
    # 뽑아야 할 원소가 가운데 이후에 있을 때
    elif number.index(target[0]) > len(number) // 2:
        while True:
            number.rotate(1)
            cnt += 1
            if target[0] == number[0]:
                break

print(cnt)
