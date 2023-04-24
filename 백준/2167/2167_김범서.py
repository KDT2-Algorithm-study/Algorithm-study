import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = [[0 for i in range(m)] for j in range(n)]
sums = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
	number[i] = list(map(int, input().split()))
	if i == 0:
		for j in range(m):
			sums[i][j] = number[i][j]
	else:
		for j in range(m):
			sums[i][j] = sums[i - 1][j] + number[i][j]

k = int(input())

for l in range(k):
	i, j, x, y = map(int, input().split())
	result = 0
	for o in range(j - 1, y):
		result += sums[x - 1][o] - sums[i - 1][o] + number[i - 1][o]
	print(result)
