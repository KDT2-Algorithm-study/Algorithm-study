a = input()
b = input()

cnt = 0
i = 0
while i <= len(a)-len(b):
    if a[i] == b[0]:
        if a[i:i+len(b)] == b:
            cnt += 1
            i += len(b)
        else:
            i += 1
    else:
        i += 1

print(cnt)