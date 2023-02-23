from collections import deque
a, b = map(int,input().split())
l = list(map(int,input().split()))
que = deque(x for x in range(1,a+1))
cnt = 0 
for i in l:
    if que.index(i) > len(que)/2:
        while que[0]!=i:
            que.appendleft(que.pop())
            cnt +=1
    else:
        while que[0]!=i:
            que.append(que.popleft())
            cnt +=1
    
    que.popleft()

print(cnt)