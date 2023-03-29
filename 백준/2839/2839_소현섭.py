n_kilogram = int(input())
backpack = 0
while n_kilogram >= 0:
    if n_kilogram % 5 == 0:
        backpack += n_kilogram // 5
        print(backpack)
        break
    n_kilogram -= 3
    backpack += 1
else:
    print(-1)