n = list(map(int, input()))
cnt = 0

for i in range(len(n)-1):
    if(n[i] != n[i+1]):
        cnt += 1

if (cnt % 2 == 0):
    print(cnt // 2)
else:
    print((cnt+1)//2)