from collections import deque

n, k = map(int, input().split())
dq = deque(range(1, n+1))

print('<', end="")
for t in range(n) :
    for _ in range(k-1) :
        dq.append(dq.popleft())
    if t == n-1:
        break    
    print(f'{dq.popleft()}, ', end="")    

print(f'{dq.popleft()}>', end="")    

