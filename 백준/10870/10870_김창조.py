# 10870. 피보나치 수 5

import sys

n = int(sys.stdin.readline())

for i in range(n+1):
    if i == 0:
        fibo1 = 0
        fibo2 = 0
    elif i == 1:
        fibo2 = 1
    else:
        fibo1, fibo2 = fibo2, fibo1 + fibo2
        
print(fibo2)