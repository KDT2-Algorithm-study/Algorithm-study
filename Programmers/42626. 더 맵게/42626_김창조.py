# 42626. 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)    
    while True:
        s1 = heapq.heappop(scoville)
        # 최소 scoville이 K 이상인 경우, 즉 모든 scoville이 K 이상
        if s1 >= K: 
            break
        # 더 이상 섞을 음식이 없는 경우
        elif not scoville:
            return -1
        s2 = heapq.heappop(scoville)
        
        new_s = s1 + s2 * 2
        heapq.heappush(scoville, new_s)
        
        answer += 1

    return answer