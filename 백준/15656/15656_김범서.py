def dfs():
    # 수열의 길이가 m일 때 수열을 출력한다
    if len(arr) == m:
        print(*arr)
        return
    # 백트래킹
    for i in range(n):
        arr.append(number[i])
        dfs()
        arr.pop()

n, m = map(int, input().split())
number = list(map(int, input().split()))
arr = list()
number.sort()

dfs()
