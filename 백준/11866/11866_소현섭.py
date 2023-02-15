n, k = map(int, input().split())
yose_li = list(range(1, n+1))

print('<', end='')
while yose_li:
    for x in range(k - 1):
        yose_li.append(yose_li[0])
        yose_li.pop(0)
    print(yose_li.pop(0), end='')
    if yose_li:
        print(',', end=' ')
print('>')