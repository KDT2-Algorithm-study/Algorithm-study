# 11866. 요세푸스 문제 0

import sys


n, k = map(int ,sys.stdin.readline().strip().split())
lst = [i for i in range(1, n+1)]

ans_lst = []
idx = k - 1
while True:
    ans_lst.append(lst[idx])
    lst.remove(lst[idx])
    if not lst:
        break
    
    n -= 1
    idx = (idx-1+k) % n
        
print("<", end="")
print(*ans_lst, sep=", ", end="")
print(">")