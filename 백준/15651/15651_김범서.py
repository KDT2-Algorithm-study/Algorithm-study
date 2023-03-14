def dfs():
    if len(arr) == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(i + 1)
        dfs()
        arr.pop()

n, m = map(int, input().split())
arr = list()

dfs()
