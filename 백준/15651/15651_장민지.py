N, M = map(int, input().split())

def backTracking(result): 
   
    if len(result) == M:
        print(*result)
        return
   
    for i in range(1, N+1):
        
      result.append(i)
      # 재귀로 백트래킹 실행
      backTracking(result)
      result.pop()

backTracking([])