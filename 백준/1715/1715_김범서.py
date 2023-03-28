import heapq, sys

n = int(sys.stdin.readline())
card = list()
temp = 0
result = 0

for i in range(n):
    heapq.heappush(card, int(sys.stdin.readline()))

# 카드 묶음이 하나 남을 때가지 가장 작은 두 묶음을 꺼내 섞고 다시 넣는다
# 비교 횟수는 두 카드 묶음의 장수 합과 같으므로
# 카드 묶음의 합을 card에 넣고, 결과를 저장하는 변수 result에는 더한다
while len(card) > 1:
    temp =  heapq.heappop(card) + heapq.heappop(card)
    result += temp
    heapq.heappush(card, temp)

print(result)
