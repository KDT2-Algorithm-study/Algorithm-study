from collections import deque

n = int(input())
num_list = deque(_ for _ in range(1, n+1))

while len(num_list) > 1:
    num_list.popleft()
    num_list.append(num_list.popleft())

print(*num_list)