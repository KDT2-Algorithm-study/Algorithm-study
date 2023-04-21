import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    # 진출방향
    direct = [(1,0),(-1,0),(0,1),(0,-1)]
    # 각 필드 금액 무한대로 우선 설정
    rupee = [[int(1e9)] * n for _ in range(n)]
    # 시작부터 잃고 시작하는 링크
    rupee[0][0] = field[0][0]
    queue = []

    # 세로위치, 가로위치, 누적비용
    heapq.heappush(queue,(0,0,rupee[0][0]))
    while queue:
        x,y,cost = heapq.heappop(queue)

        # 해당 구역 누적 금액이 현재 누적된 금액보다 작으면 패스
        if rupee[x][y] < cost:
            continue
        
        # 각 4방향 field를 벗어나지 않게 조건 걸기
        for d in direct:
            xd, yd = x + d[0], y + d[1]
            if 0 <= xd < n and 0 <= yd < n:
                # pay 는 갈 방향의 비용 + 누적 비용
                pay = field[xd][yd] + cost
                # pay가 해당 구역의 누적 비용보다 작으면 누적비용 수정
                if pay < rupee[xd][yd]:
                    rupee[xd][yd] = pay
                    # 세로위치, 가로위치, 누적비용
                    heapq.heappush(queue,(xd,yd,pay))
    # 각 구역 최소누적비용 반환
    return rupee


case = 0
while 1:
    case += 1
    n = int(input())
    if n == 0:
        break

    field = [list(map(int,input().split())) for _ in range(n)]
    # 마지막 필드 비용 출력
    print(f'Problem {case}: {dijkstra()[-1][-1]}')