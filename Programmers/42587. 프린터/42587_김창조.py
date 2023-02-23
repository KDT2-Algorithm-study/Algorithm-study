# 42587. 프린터

def solution(priorities, location):
    answer = 0
    
    order = []
    idx = 0
    length = len(priorities)
    
    while True:
        while priorities[idx] != max(priorities):
            idx = (idx + 1) % length
            
        priorities[idx] = 0
        order.append(idx)
        
        if len(order) == length:
            break
    
    answer = order.index(location) + 1
        
    return answer