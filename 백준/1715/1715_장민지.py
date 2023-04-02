import heapq, sys
N = int(sys.stdin.readline())
numbers = []
result = 0
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))
heapq.heapify(numbers)

while len(numbers) > 1:
    cnt = heapq.heappop(numbers) + heapq.heappop(numbers)
    result += cnt
    heapq.heappush(numbers, cnt)
print(result)