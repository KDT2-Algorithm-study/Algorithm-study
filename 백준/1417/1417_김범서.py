import heapq

n = int(input())
one = int(input())

# 후보가 한 명일 때
if n == 1:
    print(0)
else:
    vote = list()
    result = 0

    # 기호 2번부터
    for i in range(n - 1):
        heapq.heappush(vote, -1 * int(input()))

    # 기호 1번을 제외한 나머지 후보 중 득표수가 가장 많은 후보의 표부터
    # 한 표씩 가져온 후 그 후보의 표를 다시 힙에 넣는다.
    # 최대 힙이므로 힙 내부의 값이 음수라는 점에 유의한다.
    while abs(vote[0]) >= (one + result):
        temp = heapq.heappop(vote)
        result += 1
        temp += 1
        heapq.heappush(vote, temp)
    
    print(result)
