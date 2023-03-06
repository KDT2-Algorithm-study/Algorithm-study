import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    # 만약 스코빌이 만족되면 멈춘다
    for i in range(len(scoville)-1) : 
        if scoville[0] >= K : break
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        heapq.heappush(scoville, food1 + food2 * 2)
        cnt += 1

    if scoville[0] >= K : return(cnt)
    else : return(-1)
    
