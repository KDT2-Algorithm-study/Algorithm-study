from collections import deque
def solution(priorities, location):
    check = []
    le = len(priorities)
    for i in range(le):
        check.append(i)
    deq = deque(priorities)
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