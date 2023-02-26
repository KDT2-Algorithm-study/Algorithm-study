from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    now, cnt = 0, 0     # now는 현재 위치, cnt는 인쇄된 문서 개수 
    while True:
        if now == len(priorities): # 한바퀴 돌았을 경우 0으로 돌아감
            now = 0
        
        if max(priorities) == priorities[0]: # 맨 앞의 문서가 우선순위가 가장 높다면
            priorities.popleft()
            cnt += 1
            if now < location: # 인쇄를 요청한 문서보다 앞에서 문서가 출력되었을 경우
                location -= 1 # 인쇄를 요청한 문서의 위치를 앞으로 당김
            elif now == location: # 인쇄를 요청한 문서가 출력되었을 경우
                break
        else:
            priorities.append(priorities.popleft()) # 맨 앞의 문서를 맨 뒤로 보냄
            now += 1
             
    return cnt