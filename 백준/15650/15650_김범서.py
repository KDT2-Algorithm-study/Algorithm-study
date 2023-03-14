def dfs(offset):
    # 결과값 리스트의 길이가 m일 때 출력한다
    if len(arr) == m:
        print(*arr)
        return
    # 백트래킹
    for i in range(offset, n):
        if not visited[i]:
            visited[i] = True
            arr.append(i + 1)
            dfs(i + 1)
            arr.pop()
            visited[i] = False

n, m = map(int, input().split())
visited = [False for i in range(n)]
arr = list()
dfs(0)
