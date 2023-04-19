from collections import deque
import sys
input = sys.stdin.readline

def dijkstra():
	# 최저비용을 저장하기 위한 2차원 리스트
	# 10**9로 초기화 한다
    rupee_lost = [[int(1e9) for i in range(n)] for j in range(n)]
    rupee_lost[0][0] = cave[0][0]
    que = deque([[0, 0]])

    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < n) and (0 <= nc < n):
				# (이미 소모된 비용 + 다음 칸에서 소모될 비용)과 최저비용 리스트에
				# 저장된 다음 칸 최저비용을 비교해 전자가 더 작으면 리스트를 갱신한다
                if rupee_lost[r][c] + cave[nr][nc] < rupee_lost[nr][nc]:
                    rupee_lost[nr][nc] = rupee_lost[r][c] + cave[nr][nc]
                    que.append([nr, nc])
    return rupee_lost[n - 1][n - 1]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

ref = 1

while True:
    n = int(input())
    if not n:
        break

    cave = [list(map(int, input().split())) for i in range(n)]
    result = dijkstra()
    print(f'Problem {ref}: {result}')
    
    ref += 1
