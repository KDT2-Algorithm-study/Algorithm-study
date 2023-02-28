import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        if len(scoville) == 1:
            if scoville[0]<K:
                return -1
        
        i = heapq.heappop(scoville)
        if i >= K:
            return cnt
        
        j = heapq.heappop(scoville)
        heapq.heappush(scoville,i+2*j)
        cnt +=1