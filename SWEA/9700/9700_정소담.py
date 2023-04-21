import heapq

for t in range(1,int(input())+1):
    p, q = map(float,input().split())
    a= [((1-p) * q, 'YES'), (p * (1-q) * q, 'NO')]
    heapq.heapify(a)
    print(f'#{t} {heapq.heappop(a)[1]}')