import heapq
import sys
input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(-n,n))


# 어제 풀었던 최소힙에서 앞에 정수에 - 를 붙힌 우선순위를 함께 넣어 숫자가 클 수록 먼저 출력이 될 수 있도록 
# 풀이했습니다.