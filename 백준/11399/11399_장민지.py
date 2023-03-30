N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
result = 0

for i in range(1, N+1):
    result += sum(numbers[0:i])
print(result)