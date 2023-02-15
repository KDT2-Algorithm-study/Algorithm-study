from collections import deque

n, k = map(int, input().split())
dq = deque(range(1, n+1))

print('<', end="")
for t in range(n-1) :
    for _ in range(k-1) :
        dq.append(dq.popleft())  
    print(f'{dq.popleft()}, ', end="")    

print(f'{dq.popleft()}>', end="")    

