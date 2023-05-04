n = 1
cnt = 0
for i in range(1,int(input())+1):
    n *= i
for j in str(n)[::-1]:
    if int(j) == 0:
        cnt += 1
    else:
        print(cnt)
        break