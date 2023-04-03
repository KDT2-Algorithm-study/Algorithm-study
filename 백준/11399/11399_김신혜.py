import sys
N = int(sys.stdin.readline())
P = sorted(list(map(int, sys.stdin.readline().split())))
result = 0
for n in range(1, N+1):
    result += sum(P[:n])
print(result)
