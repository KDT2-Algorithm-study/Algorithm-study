import heapq

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)
answer = 0
for _ in range(n-1):
    temp = heapq.heappop(card) + heapq.heappop(card)
    answer += temp
    heapq.heappush(card, temp)
print(answer)