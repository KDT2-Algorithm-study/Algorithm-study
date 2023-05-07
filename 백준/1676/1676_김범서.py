n = int(input())
mult = 1
cnt = 0

for i in range(1, n + 1):
    mult *= i

numStr = str(mult)

for i in range(len(numStr) - 1, -1, -1):
    if numStr[i] == '0':
        cnt += 1
    else:
        break

print(cnt)