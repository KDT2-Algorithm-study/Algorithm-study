fib = [0, 1]

for i in range(19):
    fib.append(fib[-1] + fib[-2])

n = int(input())
print(fib[n])
