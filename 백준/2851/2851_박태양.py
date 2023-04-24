l = []
for _ in range(10):
    l.append(int(input()))
sum = 0
for i in l:
    sum += i
    if sum>100:
        if sum-100<= 100-(sum-i):
            print(sum)
            break
        else:
            print(sum-i)
            break

else:
    print(sum)    