import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville:
        food = heapq.heappop(scoville)
        if food >= K:
            break
        elif scoville:
            food2 = heapq.heappop(scoville)
            heapq.heappush(scoville, food+food2*2)
            cnt += 1
        else:
            return -1
        
    return cnt