# 1676
N = int(input())
result = 1
while True:
    if N == 1:
        break
    result *= N
    N -= 1
cnt = 0
for i in str(result)[::-1]:
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break