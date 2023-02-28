num = int(input())
l = [50000,10000,5000,1000,500,100,50,10]
for t in range(num):
    m = int(input())
    r = [0]*8
    for i in range(8):
        if m>=l[i]:
            r[i] = m//l[i]
            m %= l[i]
    
    print(f'#{t+1}')
    print(*r)