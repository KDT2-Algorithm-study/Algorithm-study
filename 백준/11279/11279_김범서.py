import sys, heapq

n = int(sys.stdin.readline())
heap = list()

# 파이썬의 heapq는 기본적으로 최소힙이기 때문에
# 최대힙을 구현하려면 -1을 곱해준다
for i in range(n):
    command = int(sys.stdin.readline())
    if not command:
        if heap:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -1 * command)
