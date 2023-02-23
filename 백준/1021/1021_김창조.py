# 1021. 회전하는 큐

import sys
from collections import deque


n, m = map(int, sys.stdin.readline().rstrip().split())
q = deque([num for num in range(1, n+1)])

finds = map(int, sys.stdin.readline().rstrip().split())

cnt = 0
for find in finds:
    
    if q.index(find) <= len(q) // 2:
        while q[0] != find:
            cnt += 1
            q.rotate(-1)
        q.popleft()
        
    else:
        while q[0] != find:
            cnt += 1
            q.rotate(1)
        q.popleft()

print(cnt)