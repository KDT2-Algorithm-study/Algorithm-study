def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
        
    for i in range(n):
        if visited[i] == 1:
            continue
        
        visited[i] = 1
        answer += 1
        stack = [i] 
        
        while stack:
            m = stack.pop()
            if visited[m] == 0:
                visited[m] = 1
            
            for j in range(n):
                if m != j and computers[m][j] == 1:
                    computers[m][j] = 0
                    stack.append(j)
                                    
    return answer

#=======================================================

# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

# solution(n, computers)



#  def bfs(graph, start, vistited):
#         queue = deque([start])
#         visited[start] = True

#         while queue:
#             v = queue.popleft()
                  
      




