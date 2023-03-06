# 재귀
def fibo(N):
    if N<=0:
        return 0
    elif N==1:
        return 1
    return fibo(N-1) + fibo(N-2)
print(fibo(int(input())))

# 다이나믹 프로그래밍
fibo = [0,1]
n = int(input())
for i in range(2,n+1):
    fibo.append(fibo[i-2]+fibo[i-1])
print(fibo[n])
    