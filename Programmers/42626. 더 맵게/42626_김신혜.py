import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        if scoville[0] >= K:
            return cnt
        if len(scoville) == 1:
            return -1
        h0 = heapq.heappop(scoville)   # h0 = 1
        h1 = heapq.heappop(scoville)   # h1 = 2
        h3 = h0 + h1 * 2        # h3 = 5
        heapq.heappush(scoville, h3)
        cnt += 1

print(solution([1, 2, 3, 9, 10, 12], 7))