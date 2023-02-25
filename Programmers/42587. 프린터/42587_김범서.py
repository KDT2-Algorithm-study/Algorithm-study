from collections import deque

def solution(priorities, location):
    printer_que = deque()
    order = 0
    
    # 프린터 대기열에 우선순위와 문서의 원래 위치를 묶어 넣는다
    for i in range(len(priorities)):
        printer_que.append((priorities[i], i))

    while True:
        # 대기열에서 우선순위가 가장 높은 문서를 기준으로 한다
        ref = max(printer_que)
        # 대기열 가장 앞의 문서를 확인한다
        now = printer_que.popleft()
        # 만약 가장 앞의 문서가 가장 우선순위가 높다면
        if now[0] == ref[0]:
            # 순서에 1을 더한다
            order += 1
            # 가장 앞의 문서의 원래 위치가 location과 같다면
            # order를 반환한다
            if now[1] == location:
                return order
        # 우선순위가 가장 높은 문서가 아니라면 가장 뒤로 보낸다
        else:
            printer_que.append(now)
