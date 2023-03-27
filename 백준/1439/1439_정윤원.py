num = input()
up, down = 0, 0
a = -1

for i in num:
    if i != a:
        a = i
        if i == '0':
            down += 1
        else:
            up += 1

print(min(down, up))
num = input()
up, down = 0, 0
a = -1

for i in num:
    if i != a:
        a = i
        if i == '0':
            down += 1
        else:
            up += 1

print(min(down, up))
