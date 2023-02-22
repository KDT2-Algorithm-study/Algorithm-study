from collections import deque
n = int(input())
dq = deque(range(1, n+1))

for i in range(n-1) :
    dq.popleft()
    a = dq.popleft()
    dq.append(a)
print(*dq)