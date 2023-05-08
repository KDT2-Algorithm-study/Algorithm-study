# 1676. 팩토리얼 0의 개수

N = int(input())

factorial = 1
for i in range(2, N+1):
    factorial *= i
    
answer = 0
while factorial > 0:
    if factorial % 10:
        break
    factorial //= 10
    answer += 1

print(answer)