N, M = map(int, input().split())

# 방문 리스트 만들기
visited = [False]*(N+1)

def backTracking(result):
    # M과 리스트의 개수가 같으면 출력 후 함수 종료
    if len(result) == M:
        print(*result)
        return
    
    # 방문 전 and 빈 리스트이거나 or
    # 방문 전 and 담아놓은 결과가 담을 것보다 작으면 담기
    for i in range(1, N+1):
        if (visited[i]== False) and (len(result)==0 or i > result[-1]):
            visited[i] = True
            result.append(i)
            # 재귀로 백트래킹 실행
            backTracking(result)
            # 재귀 끝난 뒤 직전 값 제거(1 2, 1 3, 1 4인 부분에서 2,3,4출력하기 위해서)
            visited[i] = False
            result.pop()

backTracking([])