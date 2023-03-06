import sys
n = int(sys.stdin.readline())   # 10
a, b = 0, 1
for _ in range(n):
    number = a + b
    a, b = b, number
print(a)