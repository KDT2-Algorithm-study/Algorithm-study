
def fibonacci(n):
    fibo = [(1,0),(0,1)] 
    for i in range(2,n+1):
        x1,y1 = fibo[i-1]
        x2,y2 = fibo[i-2] 
        fibo.append((x1+x2,y1+y2)) 
    return fibo[n]

for _ in range(int(input())):
    print(*fibonacci(int(input())))