num = int(input())
count = 0

while num >= 0:
    if num % 5 == 0:
        count += int(num//5)
        print(count)
        break
    num = num - 3
    count += 1

    if count < 0:
        print(-1)
        break