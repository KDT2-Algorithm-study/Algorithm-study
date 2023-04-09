def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i] == False:
            stack = [i]
            visited[i] = True
            while stack:
                cur = stack.pop()
                for j in range(n):
                    if cur == j:
                        continue
                    elif computers[cur][j] == 1 and visited[j] == False:
                        visited[j] = True
                        stack.append(j)
            answer += 1        
    return answer