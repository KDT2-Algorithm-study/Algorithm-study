# 43162. 네트워크

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i]:
            continue
        
        answer += 1
        stack = [i]
        visited[i] = True
        while stack:
            v = stack.pop()
            for j in range(n):
                if computers[v][j] and not visited[j]:
                    visited[j] = True
                    stack.append(j)
                
    return answer