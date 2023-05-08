import sys
input = sys.stdin.readline

# 도시, 버스노선
n, m = int(input()), int(input())
INF = int(1e9)
# 요금 비교 위해 무한대수로 초기설정
bus = [[INF]*(n+1) for _ in range(n+1)]

# a->b 로 가는 요금 중 작은 금액
for _ in range(m):
    a, b, c = map(int,input().split())
    bus[a][b] = min(bus[a][b], c)

# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 출발, 도착이 같으면 요금이 0 
            if a == b:
                bus[a][b] = 0
            bus[a][b] = min(bus[a][b], bus[a][k] + bus[k][b])

# 금액이 무한대인 곳은 도달 할 수 없는 곳 이므로 0으로 바꿔서 한 줄씩 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if bus[a][b] == INF:
            bus[a][b] = 0
    print(*bus[a][1:])