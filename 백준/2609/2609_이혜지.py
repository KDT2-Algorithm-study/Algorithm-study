li = list(map(int, input().split()))

minn = min(li)
maxx = max(li)
gcd = minn

for _ in range(minn) :
    if minn % gcd == 0 and maxx % gcd == 0 :
        break
    else :
        gcd -= 1
       
lcm = maxx // gcd * minn 

print(gcd, lcm, sep="\n")
