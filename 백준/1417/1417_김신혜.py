import heapq
import sys
n = int(sys.stdin.readline())
my = int(sys.stdin.readline())
cnt = 0
h = []
for i in range(n-1):
    # 투표수를 음수로 heapq에 저장해서 가장 큰 수가 먼저 pop하도록 한다.
    heapq.heappush(h, -int(sys.stdin.readline()))
    
while True:
    if n == 1:
        break
    # 가장 큰 투표수를 얻는다.
    vote = heapq.heappop(h)
    if my <= -vote:
        # 내 득표수를 하나 가져올 때마다 cnt
        my += 1
        cnt += 1
        heapq.heappush(h, -1 * vote + 1)
    # 내 득표수가 더 높으면 stop
    else:
        break
print(cnt)
