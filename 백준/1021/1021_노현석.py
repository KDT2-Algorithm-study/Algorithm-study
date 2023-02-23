from collections import deque

n, m = map(int, input().split())
q = deque([i for i in range(1, n+1)])
target_idx = list(map(int, input().split()))
res = 0

for i in target_idx:
    while 1:
        if q.index(i) == 0:
            q.popleft()
            break
        if q.index(i) <= len(q) // 2:  #타겟이 중앙보다 왼쪽이면 2번연산
            q.rotate(-1)
            res += 1
        else:
            q.rotate(1)
            res += 1
print(res)
