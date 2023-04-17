import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for i in range(v + 1)]
result = [int(1e9) for i in range(v + 1)]
result[k] = 0
que = [(0, k)]

for i in range(e):
	a, b, c = map(int, input().split())
	heapq.heappush(graph[a], (c, b))

while que:
	length, point = heapq.heappop(que)
	while graph[point]:
		next_length, next_point = heapq.heappop(graph[point])
		if length + next_length < result[next_point]:
			heapq.heappush(que, (length + next_length, next_point))
			result[next_point] = length + next_length

for i in range(1, v + 1):
	print('INF' if result[i] == int(1e9) else result[i])
