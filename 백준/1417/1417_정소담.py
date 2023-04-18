import heapq
candidate = [[-int(input()),-i] for i in range(int(input()))]
cnt = 0

while 1:
    heapq.heapify(candidate)
    if candidate[0][1] == 0:
        print(cnt)
        break
    else:
        cnt += 1
        n = heapq.heappop(candidate)
        n[0] += 1
        heapq.heappush(candidate,n)
        for i in candidate:
            if i[1] == 0:
                i[0] -= 1