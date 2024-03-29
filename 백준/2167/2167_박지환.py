import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
dp = [[0] * (m + 1) for _ in range(n+1)]

for r in range(1, n+1):
    for c in range(1, m+1):
        dp[r][c] = arr[r-1][c-1] + dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1]

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1] )