from collections import deque
N = int(input())
list1 = deque(range(1, N + 1))

while len(list1) > 1 :
    list1.popleft()
    list1.append(list1.popleft())
    
print(list1[0])
