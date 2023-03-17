def dfs(offset):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(offset, n):
        arr.append(i + 1)
        dfs(i)
        arr.pop()

n, m = map(int, input().split())
arr = list()

dfs(0)
