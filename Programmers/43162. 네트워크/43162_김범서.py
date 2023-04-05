from collections import deque


def solution(n, computers):
    chk = [False for i in range(n)]
    answer = 0
    for i in range(n):
        if not chk[i]:
            que = deque([i])
            chk[i] = True
            while que:
                now = que.popleft()
                for j in range(n):
                    if j == now: continue
                    if computers[now][j] and not chk[j]:
                        que.append(j)
                        chk[j] = True
            answer += 1
    return answer
