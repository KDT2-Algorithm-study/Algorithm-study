import sys
input = sys.stdin.readline

# n,m = map(int,input().split())
# lst = [list(map(int,input().split())) for _ in range(n)]
# num = int(input())
# for _ in range(num):
#     sum = 0
#     x1, y1, x2, y2 = map(int,input().split())
#     for i in range(x1-1,x2):
#         for j in range(y1-1,y2):
#             sum += lst[i][j]
#     print(sum)
# 시간초과

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
prefix_sum = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j] + lst[i][j]

num = int(input())
for _ in range(num):
    sum = 0
    x1, y1, x2, y2 = map(int,input().split())
    result = prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]
    print(result)