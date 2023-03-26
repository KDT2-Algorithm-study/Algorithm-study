string = input()
check = input()
result = ""
cnt = 0

for i in string:
    result += i
    if check in result:
        result = ""
        cnt += 1
print(cnt)