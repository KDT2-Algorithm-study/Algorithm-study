import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    for i in range(len(scoville)-1) : 
        if scoville[0] >= K : break # 만약 스코빌이 만족되면 멈춘다
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        cnt += 1

    if scoville[0] >= K : return(cnt)
    else : return(-1)