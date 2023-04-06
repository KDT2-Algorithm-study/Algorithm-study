# 13333. Q-인덱스

n = int(input())
nums = list(map(int, input().split()))

q_idx = n
while True:
    cnt = 0
    for num in nums:
        if num >= q_idx: cnt += 1
        
    if cnt >= q_idx:
        break
    
    q_idx -= 1
    
print(q_idx)