import sys
N = int(sys.stdin.readline())
def f(n):
    N = n
    if n == 0:
        return 1
    else:
        return n * f(n-1)
print(f(N))
