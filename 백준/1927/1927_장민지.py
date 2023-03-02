import heapq
import sys
N = int(input())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline())
    if number != 0:
        heapq.heappush(numbers, number)
    else:
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print(0)