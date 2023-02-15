from collections import deque
a,b = map(int,input().split())
l = deque(x for x in range(1,a+1))
yo=[]
while len(l) !=1:
    for i in range(b-1):
        l.append(l.popleft())
    yo.append(l.popleft())    
yo.append(l[0])

result = ', '.join(map(str,yo))
print(f'<{result}>')