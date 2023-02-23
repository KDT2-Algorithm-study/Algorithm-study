from collections import deque

n, m = map(int, input().split())
queue = deque(range(1, n+1))
command = list(map(int, input().split()))

total = 0
for i in command:
    cnt = 0
    while queue[0] != i:
        queue.rotate(1)
        cnt += 1
    
    total += min(len(queue) - cnt, cnt)
    queue.popleft()

print(total)