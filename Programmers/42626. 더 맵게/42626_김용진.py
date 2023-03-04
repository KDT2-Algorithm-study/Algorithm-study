# 더 맵게

import heapq

lst = []
cnt = 0
def solution(scoville, K):
    global cnt
    for i in scoville:
        heapq.heappush(lst,i)
    
    while 1:
        if len(scoville) == 1:
            break
        
        first = heapq.heappop(lst)
        if first >= K:
            break
        second = heapq.heappop(lst)
        mix = first + second * 2
        heapq.heappush(lst,mix)
        cnt += 1
        
        if len(lst) == 0:
            break            
        elif cnt == len(scoville)-1:
            break
        
    if lst[0] > K:
        return cnt
    else:
        return -1