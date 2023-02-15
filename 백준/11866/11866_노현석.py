from collections import deque
n, k = map(int, input().split())
q = deque(list(range(1, n+1)))
res = []

while q:
    q.rotate(-k + 1)
    res.append(str(q.popleft()))

print('<', ', '.join(res),'>', sep='')