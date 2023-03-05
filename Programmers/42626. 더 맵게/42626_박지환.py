import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        t = heapq.heappop(scoville) # 스코빌에서 가장 작은 숫자가
        if t < K: # 기준치보다 작은 경우
            if len(scoville) == 0: # 더이상 남아있지 않은 경우
                return -1
            else: # 남아있는 경우
                heapq.heappush(scoville, t + heapq.heappop(scoville)*2) # 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
                answer += 1
        else:
            heapq.heappush(scoville, t) # 기준치보다 큰 경우
            return answer
    
#===========================================================================================================================================================
        
import heapq

scovile = list(map(int, input().split()))
K = int(input())
heapq.heapify(scovile)
cnt = 0

while True:
    t = heapq.heappop(scovile) # 스코빌에서 가장 작은 숫자가
    if t < K: # 기준치보다 작은 경우
        if len(scovile) == 0: # 더이상 남아있지 않은 경우
            print(-1)
            break
        else: # 남아있는 경우
            heapq.heappush(scovile, t + heapq.heappop(scovile)*2) # 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
            cnt += 1
    else:
        heapq.heappush(scovile, t) # 기준치보다 큰 경우
        print(cnt)
        break