from collections import deque

def solution(priorities, location):
    answer = 0
    idx = [0] * len(priorities)
    idx[location] = 1
    
    lst_ = deque(priorities)
    idx_ = deque(idx)
    while 1:
        if lst_[0] == max(lst_):
            answer += 1

            if idx_[0]:
                print(answer)
                break
            else:
                lst_.popleft()
                idx_.popleft()
        else:
            lst_.rotate(-1)
            idx_.rotate(-1)
    return answer