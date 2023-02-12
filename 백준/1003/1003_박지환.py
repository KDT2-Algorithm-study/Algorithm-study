T = int(input())

def fibonacci(n):
    zero, one = 0, 1
    for i in range(n):
        zero, one = one, zero + one
    return zero

for _ in range(T):
    n = int(input())

    if n == 0:
        print(1, 0)
    else:
        print(fibonacci(n-1), fibonacci(n))
