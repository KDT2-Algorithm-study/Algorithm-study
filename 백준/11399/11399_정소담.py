input()
n = sorted(list(map(int,input().split())))
m = []
cnt = 0
for i in n:
    cnt += i
    m.append(cnt)
print(sum(m))