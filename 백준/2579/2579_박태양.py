num = int(input())
l = []
ans = [0]*num
for i in range(num):
    a = int(input())
    l.append(a)

ans[0] = l[0]
if num>=2:
    ans[1] = l[1]+l[0]
if num>=3:
    ans[2] = max(l[0]+l[2],l[2]+l[1])
if num>=4:
    for i in range(3,num):
        ans[i] = max(l[i]+ans[i-3]+l[i-1],l[i]+ans[i-2])
print(ans[-1])
