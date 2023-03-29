num = int(input())
count = 0

while 1:
    if num % 5 == 0:
        count += num // 5
        print(count)
        break
    num -= 3
    count += 1

    if num < 0:
        print(-1)
        break