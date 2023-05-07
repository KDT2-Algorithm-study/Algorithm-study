import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[int(1e9) for i in range(n)] for j in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    bus[a - 1][b - 1] = min(bus[a - 1][b - 1], c)

for i in range(n):
    bus[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            bus[j][k] = min(bus[j][k], bus[j][i] + bus[i][k])

for i in range(n):
    for j in range(n):
        if bus[i][j] == int(1e9):
            bus[i][j] = 0

for element in bus:
    print(*element)