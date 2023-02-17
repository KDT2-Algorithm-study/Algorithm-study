a,b= map(int,input().split())
l = []
for _ in range(a):
    l.append(input())

k = 32
for x in range(0,a-7):
    for y in range(0,b-7):
        t1=0
        t2=0
        for i in range(x,8+x):
            for j in range(y,8+y):
                    if (i+j)%2==0:
                        if l[i][j] !='B':
                            t1+=1
                        if l[i][j] != 'W':
                            t2+=1
                    else:
                        if l[i][j] != 'W':
                            t1+=1
                        if l[i][j] !='B':
                            t2+=1

        if t1<=t2 and k>t1:
            k = t1
        elif t1>=t2 and k>t2:
            k = t2
print(k)