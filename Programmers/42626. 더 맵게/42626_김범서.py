import heapq

def solution(scoville, K):
    # 입력된 리스트를 최소 힙으로 변환한다
    heapq.heapify(scoville)
    answer = 0
    
    while True:
        # 스코빌 지수가 가장 작은 음식의 수치가 K 이상이면
        # 음식을 섞은 횟수를 반환한다
        if scoville[0] >= K:
            return answer

        # 음식을 다 섞었는데도 스코빌 지수가 K 이상이 아니라면
        # -1을 반환한다
        if len(scoville) == 1:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + second * 2
        heapq.heappush(scoville, mixed)
        answer += 1
