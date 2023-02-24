from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    while priorities:
        if priorities[0] != max(priorities):
            priorities.append(priorities.popleft())
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
        elif priorities[0] == max(priorities):
            priorities.popleft()
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1
