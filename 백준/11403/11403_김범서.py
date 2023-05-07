n = int(input())
adj = [[0 for i in range(n)] for j in range(n)]
result = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    adj[i] = list(map(int, input().split()))

for i in range(n):
    stack = [i]
    visited = [False] * n

    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True
            for j in range(n):
                if adj[now][j] == 1:
                    result[i][j] = 1
                    stack.append(j)

for i in range(n):
    print(*result[i])