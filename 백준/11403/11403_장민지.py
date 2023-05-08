n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
 
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
                
for g in graph:
    print(*g)
# 이해가 되지 않아서 구글링으로.... 
# 플로이드-워셜 알고리즘을 아직 백프로 이해하진 못했습니다ㅠㅠ
