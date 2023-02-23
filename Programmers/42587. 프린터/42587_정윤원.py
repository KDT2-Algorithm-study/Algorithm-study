from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    cnt = 0
    max_proir = max(priorities)

    while True :
        print(location)
        if priorities[0] != max_proir :
            priorities.append(priorities.popleft())

            if location == 0 : location += len(priorities) - 1
            else : location -= 1
            # location += len(priorities) - 1 if location == 0 else - 1
            
        else : 
            cnt += 1

            if location == 0 : return cnt
            else : location -= 1

            priorities.popleft()
            max_proir = max(priorities)