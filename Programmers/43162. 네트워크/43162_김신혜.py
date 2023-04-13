def solution(n, computers):
    visited = [False] * n #방문기록장
    print(visited)
    answer = 0
    for i in range(n): # n은 3이니까 0 1 2
        if visited[i] == True: # if visited[i]:
            continue
       #else:
        visited[i] = True  #방문하면 True로 기록
        stack = [i] # i = 0이 들어있는 리스트
        answer += 1
        
       #dfs의 시작
        while len(stack) != 0: # s이 비어있지 않을 때
            a = stack.pop() # stack 제일 마지막 요소 출력 + 삭제
            for j in range(n): # 0 1 2
                if computers[a][j] == 1 and visited[j] == False:
                    visited[j] = True
                    stack.append(j)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
