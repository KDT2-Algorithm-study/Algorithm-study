a,b=map(int,input().split())
l = []
coin = 0
for i in range(a):
    l.append(int(input()))
for j in reversed(l):
    if b>=j:
        coin +=b//j
        b%=j 
print(coin)