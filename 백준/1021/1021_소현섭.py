from collections import deque

def extract(list_a):
    return list_a.popleft()

def left_move(list_b):
    return list_b.append(list_b.popleft())

def right_move(list_c):
    return list_c.appendleft(list_c.pop())

n, m = map(int, input().split())
atom = deque(list(range(1, n+1)))
num_list = deque(list(map(int, input().split())))
answer = 0

while num_list:
    if atom[0] == num_list[0]:
        extract(atom)
        num_list.popleft()
    elif (len(atom)//2) >= atom.index(num_list[0]):
        left_move(atom)
        answer += 1
    else:
        right_move(atom)
        answer += 1
print(answer)