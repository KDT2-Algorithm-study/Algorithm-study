# 네트워크
# 현섭님 코드를 참고해서 풀었습니다..
def solution(n, computers):
    visited = [False]*n
    answer = 0
    for i in range(0,n):
        if visited[i] == False:
            dfs(n,computers, i, visited)
            answer += 1
            
    return answer


def dfs(n, computers, i, visited):
    visited[i] = True
    
    for x in range(0,n):
        if visited[x] == False and computers[i][x] == True:
           dfs(n, computers, x, visited) 
    return visited