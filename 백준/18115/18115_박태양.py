from collections import deque
a = int(input())
l = list(map(int,input().split()))
ans = []
deq = deque([])
ans2 = deque([])
a = len(l)
for i in range(a):
    k = a-i
    if l[i] == 1:
        if deq:
            deq.appendleft(k)
            ans +=deq
            deq.clear()
        else:
            ans.append(k)
    elif l[i] == 2:
        deq.append(k)
    else:
        ans2.appendleft(k)

print(*(ans),end=' ')
if deq:
    print(*(deq),end=' ')
print(*(ans2),end=' ')