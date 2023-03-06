n = [0,1]
m = int(input())
for i in range(m):
    n.append(n[-1]+n[-2])
print(n[m])
