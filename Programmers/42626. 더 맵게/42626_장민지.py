import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville) # 정렬시
    if scoville[0] >= K: # 맨 앞 즉 최솟값이 K보다 클 경우
        return cnt # return
    
    while True:
        if len(scoville) == 1: # 길이가 1이면 (즉, K이상으로 만들 수 없는 경우)
            return -1 # -1 return
        num1 = heapq.heappop(scoville) # 최솟값
        num2 = heapq.heappop(scoville) # 2번째 최솟값
        result = num1 + num2 * 2
        heapq.heappush(scoville, result)
        cnt += 1
        if scoville[0] >= K: # result 값으로 조건을 줄 경우 {1,2,3} k = 5인 경우 예외 케이스 발생
            return cnt     