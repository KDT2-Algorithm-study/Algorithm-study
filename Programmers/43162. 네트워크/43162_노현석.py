def dfs(k, visited, n, computers):
    visited[k] = True
        
    for i in range(n):
        if not visited[i] and computers[k][i] == 1:
            dfs(i, visited, n, computers)
        

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, n, computers)
            answer += 1
    return answer