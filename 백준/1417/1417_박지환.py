n = int(input())
dasom = int(input())
candidate = [int(input()) for _ in range(n-1)]
cnt = 0

while candidate:
    candidate = sorted(candidate, reverse=True)
    
    if dasom > max(candidate):
        break
    else:
        dasom += 1
        candidate[0] -= 1
        
    cnt += 1

print(cnt)