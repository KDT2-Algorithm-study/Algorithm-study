import heapq
import sys
input = sys.stdin.readline

# 도시개수, 버스개수
n, m = int(input()), int(input())

# bus 리스트의 각 인덱스는 버스의 출발도시
bus = [[] for _ in range(n+1)]
# 버스노선 수 만큼 입력받음
for _ in range(m):
    # 출발도시, 도착도시, 비용
    x, y, z = map(int,input().split())
    # 출발도시.append(도착도시, 비용)
    bus[x].append((y,z))

# 내가 출발하는 도시, 도착하는 도시
start, end = map(int,input().split())

# 다익스트라
def dijkstra(bus, start):
    # 각 도착 도시의 비용을 무한대의 수로 설정
    cost = [int(1e9)] * (n+1)
    # 내가 출발하는 도시까지 도착하는데 들어가는 누적비용은 0
    cost[start] = 0
    queue = []
    # 큐에 [누적비용,도착도시] 추가
    heapq.heappush(queue, [cost[start], start])

    # 큐에 요소가 있는 동안 반복
    while queue:
        # [누적비용,도착도시]
        cd, cn = heapq.heappop(queue)
        # 해당 버스노선 도착 도시의 비용이 해당 버스노선 출발도시에 누적된 비용보다 작으면 continue
        if cost[cn] < cd:
            continue
        
        # 도착도시, 비용 in 출발도시가 같은 노선의 버스들
        for tn,td in bus[cn]:
            # 돈 = 출발도시에 오기까지 누적된 비용 + 앞으로 도착도시까지 갈 때 드는 비용
            money = cd + td
            # 만약 기존에 도착도시까지 가는데 들었던 비용이 더 크면
            if cost[tn] > money:
                # 도착도시 비용 교체
                cost[tn] = money
                # 큐에 [누적비용, 도착도시] 추가
                heapq.heappush(queue,(money,tn))
    # 내가 도착할 도시의 비용 return
    return cost[end]

print(dijkstra(bus,start))