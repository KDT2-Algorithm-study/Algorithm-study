n = [int(input()) for _ in range(10)]
cnt = 0
for i in range(10):
    cnt += n[i]
    if cnt >= 100:
        m =  cnt - n[i]
        if cnt - 100 > 100 - m:
            print(m)
        elif cnt - 100 <= 100 - m:
            print(cnt)
        break
if cnt < 100:
    print(cnt)