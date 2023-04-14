from collections import deque
import sys, heapq

n, m = map(int, sys.stdin.readline().split())
computer = [[] for i in range(n + 1)]
result = list()
answer = list()
before = 0
que = deque()

def bfs(point):
    global cnt
    visited = [False] * (n + 1)
    visited[point] = True
    que.append(point)

    while que:
        now = que.popleft()
        for item in computer[now]:
            if not visited[item]:
                que.append(item)
                visited[item] = True
                cnt += 1

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    computer[b].append(a)

for i in range(1, n + 1):
    cnt = 0
    bfs(i)
    heapq.heappush(result, (-1 * cnt, i))

while result:
    temp = heapq.heappop(result)
    if not answer:
        answer.append(temp[1])
    elif before == temp[0]:
        answer.append(temp[1])
    else:
        break
    before = temp[0]

print(*answer)
