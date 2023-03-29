# 2839. 설탕 배달

n = int(input())
for i in range(n//5, -1, -1):
    temp = n - 5 * i
    if temp % 3 == 0:
        print(i + temp // 3)
        break
else:
    print(-1)