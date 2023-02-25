from collections import deque
import copy
def solution(priorities, location):
    check = []
    le = len(priorities)
    for i in range(le):
        check.append(i)
    deq = copy.deepcopy(priorities)
    deq = deque(deq)
    check = deque(check)
    while True:
        a = deq.popleft()
        num = check.popleft()
        for i in deq:
            if i>a:
                deq.append(a)
                check.append(num)
                break
        else:
            if num == location:
                answer = le - len(check)
                break
    return answer