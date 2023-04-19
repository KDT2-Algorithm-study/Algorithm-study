T = int(input())
li = []
cnt = 0

dasom = int(input())

for _ in range(1, T) :
    a = int(input())
    li.append(a)

li = sorted(li)

if len(li) != 0:
    while True :    
        if dasom >li[-1] :
            break
        
        dasom += 1
        li[-1] -= 1
        cnt += 1
        li = sorted(li)
print(cnt)


    