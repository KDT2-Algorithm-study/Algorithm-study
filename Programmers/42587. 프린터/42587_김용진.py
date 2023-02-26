# 프린터

from collections import deque
def solution(priorities, location):
    dq= deque([(v,i) for i,v in enumerate(priorities)]) # enumerate로 priorities의 번호를 부여
    idx = []
    stack = []
    while 1:
        mdq = max([x[0] for x in dq]) # 번호가 부여된 튜플값중 원래 priorities의 값중 max값을 mdq에 저장
        z = dq.popleft() # dq값중 0번값을 z의 저장
        if mdq != z[0]: # mdq 값과 튜플 z의 [0]값이 같지 않으면
            dq.append(z) # dq의 가장 마지막에 저장
        elif mdq == z[0]: # 만약 같으면
            stack.append(z) # 해당 값을 stack리스트에 저장
            
        if len(dq) == 0: # 계속 반복하고 dq의 리스트가 빈다면
            break # while문 break
    for a,b in stack: # stack의 튜플 값중 priorities 값을 a에 저장 enumerate로 순서를 부여한 값을 b에 저장 
        idx.append(b) # 순서들만 idx 리스트에 순서대로 저장
    return (idx.index(location)+1) # 해당 리스트에 location 값의 인덱스 위치를 찾고 +1