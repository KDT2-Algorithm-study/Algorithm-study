import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for i in range(n + 1)]
result = [int(1e9)] * (n + 1)

for i in range(m):
    start, end, cost = map(int, input().split())
    bus[start].append((cost, end))

initial, final = map(int, input().split())
que = [(0, initial)]
result[0] = 0

# 다익스트라
while que:
    length, point = heapq.heappop(que)
    if result[point] < length: continue
    for next_length, next_point in bus[point]:
        # 최단거리 갱신하기
        if length + next_length < result[next_point]:
            heapq.heappush(que, (length + next_length, next_point))
            result[next_point] = length + next_length

print(result[final])
