
num = int(input())
lst = []
for i in range(num):
    lst.append(list(map(int,input().split())))

maxval = max(map(max,lst))
move = [(1,0),(-1,0),(0,1),(0,-1)]
result = 0
for i in range(0,maxval+1):
    check = [[False for _ in range(num)] for _ in range(num)]
    stack = []
    cnt = 0
    for j in range(num):
        for k in range(num):
            if lst[j][k] <= i:
                check[j][k] = True
    
    for j in range(num):
        for k in range(num):
            if check[j][k] == False:
                stack.append((j,k))
                cnt +=1
            while stack:
                x,y = stack.pop()
                for dx,dy in move:
                    if 0<=x+dx<num and 0<=y+dy<num:
                        if check[x+dx][y+dy] == False:
                            check[x+dx][y+dy] = True
                            stack.append((x+dx,y+dy))
    
    
    result = max(result,cnt)

print(result)
    